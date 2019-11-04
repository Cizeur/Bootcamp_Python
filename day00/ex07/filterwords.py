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
output = "".join([" " if x in string.punctuation
                 else x for x in args[0]]).split()
output = [x for x in output if len(x) > size]
if not len(output):
    error()
print(output)
