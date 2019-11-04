import sys

args = sys.argv
args.pop(0)
args = list(map(str.strip, args))
sentence = " ".join(args)
sentence = list(sentence)
sentence.reverse()
output = list()
for elt in sentence:
    if elt.isupper():
        output.append(elt.lower())
    else:
        output.append(elt.upper())
if output:
    output = ''.join(output)
    print(output)
