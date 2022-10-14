# importing libraries
import librosa
import numpy as np
from scipy.io.wavfile import write

def encoding():
    print('Make sure that cover audio is larger than message audio.')

    # reading data i.e. numpy array of wav file and sr i.e. that is sampling rate of wav file
    try:
        data1, sr1 = librosa.load(input('Please enter cover audio file name: '))
    except:
        print("Please input correct file name")
        exit()
    try:
        data2, sr2 = librosa.load(input('Please enter message file name: '))
    except:
        print("Please input correct file name")
        exit()
    # since numpy array of different size cannot be subtracted making smaller array as equal to bigger one
    extra = np.zeros(np.size(data1) - np.size(data2))
    datap = np.append(data2, extra)

    # dividing message array to reduce its effect on o/p
    datap = datap / 25

    # hiding message in main audio
    op = np.add(data1, datap)

    # giving wav o/p
    scaled = np.int16(op / np.max(np.abs(op)) * 32767)
    write('enco.wav', sr1, scaled)
    exit()

def decoding():
    # reading data i.e. numpy array of wav file and sr i.e. that is sampling rate of wav file
    try:
        data1, sr1 = librosa.load(input('Please enter encoded file\'s name: '))
    except:
        print("Please input correct file name")
        exit()
    try:
        data2, sr2 = librosa.load(input('Please enter cover audio file name: '))
    except:
        print("Please input correct file name")
        exit()
    # since numpy array of different size cannot be subtracted making smaller array as equal to bigger one
    extra = np.zeros(np.size(data1) - np.size(data2))
    datap = np.append(data2, extra)

    # extracting message from cover audio
    op = np.subtract(data1, datap)

    # amplifying message
    op = op * 25

    # giving wav o/p
    scaled = np.int16(op / np.max(np.abs(op)) * 32767)
    write('deco.wav', sr1, scaled)
    exit()



print("**************Audio on audio steganography**************\n")
print("linkedin:https://www.linkedin.com/in/rishi-raturi/ \n")
print("github: https://github.com/RishiRats \n")
print("******************************")
print("Please select your option\n")
print("******************************")
print("[0] Encoding\n")
print("[1] Decoding\n")
a = input(("Option: "))
if a == str("0"):
    encoding()
elif a == str("1"):
    decoding()
elif print("Please rerun the code and select proper option."):
    exit()

