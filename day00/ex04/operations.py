import sys


usage = """Usage: python operations.py
Example:
    python operations.py 10 3"""

def error_usage(error):
    if error:
        print (error)
    print (usage)
    exit(1)

args = sys.argv
args.pop(0)
if not len(args):
    error_usage("")
if len(args) < 2:
    error_usage("InputError: not enough arguments")
if len(args) > 2:
    error_usage("InputError: too many arguments")
try:
    left = int(args[0])
    right = int(args[1])
except Exception:
    error_usage("InputError: only numbers")
print("%-13s%i" % ("Sum:", left + right))
print("%-12s%i" % ("Difference:", left - right))
print("%-13s%i" % ("Product:", left * right))
if right:
    divide = float(left) / float(right)
    print("%-12s" % ("Quotient:"), divide)
    print("%-11s%i" % ("Remainder:", left % right))
else:
    print("%-13s%s" % ("Quotient:", "ERROR (div by zero)"))
    print("%-11s%s" % ("Remainder:", "ERROR (modulo by zero)"))