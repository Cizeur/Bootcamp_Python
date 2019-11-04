import sys


def error():
    print("ERROR")
    exit(1)


args = sys.argv
args.pop(0)

morse_dictionnary = {'A': '.-', 'B': '-...',
                     'C': '-.-.', 'D': '-..', 'E': '.',
                     'F': '..-.', 'G': '--.', 'H': '....',
                     'I': '..', 'J': '.---', 'K': '-.-',
                     'L': '.-..', 'M': '--', 'N': '-.',
                     'O': '---', 'P': '.--.', 'Q': '--.-',
                     'R': '.-.', 'S': '...', 'T': '-',
                     'U': '..-', 'V': '...-', 'W': '.--',
                     'X': '-..-', 'Y': '-.--', 'Z': '--..',
                     '1': '.----', '2': '..---', '3': '...--',
                     '4': '....-', '5': '.....', '6': '-....',
                     '7': '--...', '8': '---..', '9': '----.',
                     '0': '-----', ' ': ' '}

stri = "SOS"
args = list(map(str.strip, args))
try:
    sentence = " ".join(args).upper()
    sentence = " ". join([x.strip() for x in sentence.split()
                         if x.strip() != ""])
    sentence = "+".join([morse_dictionnary[x] for x in sentence])
    sentence = "/".join([x.strip() for x in sentence.split()
                        if x.strip() != ""])
    sentence = sentence.replace("+", " ")
except Exception:
    error()
if sentence:
    print(sentence)
