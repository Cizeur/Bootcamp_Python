import sys
import string


def error():
    print("ERROR")
    exit(1)


args = sys.argv
args.pop(0)

if len(args) != 2:
    error()
try:
    size = int(args[1])
except ValueError:
    error()
try:
    test = int(args[0])
    error()
except ValueError:
    output = "".join([" " if x in string.punctuation
                      else x for x in args[0]]).split()
    output = [x for x in output if len(x) > size]
    print(output)
