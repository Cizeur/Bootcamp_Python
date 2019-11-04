import sys


args = sys.argv
args.pop(0)
if not len(args):
    exit(0)
if len(args) != 1:
    print("ERROR")
    exit(1)
try:
    val = int(args[0])
except Exception:
    print("ERROR")
    exit(1)
if not val:
    print("I'm Zero.")
elif val % 2:
    print("I'm Odd.")
else:
    print("I'm Even.")
