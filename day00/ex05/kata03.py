

phrase = "The right format"

if isinstance(phrase, str):
    print("{:->42.42}".format(phrase), end='')
else:
    print("Not a string")
