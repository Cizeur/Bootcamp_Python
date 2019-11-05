import random

def generator(text, sep = "", option = None):
    """Option is an optional arg, sep is mandatory"""
    if not isinstance(text, str):
        yield ("ERROR")
        return
    if not isinstance(sep, str) or not sep:
        yield ("ERROR")
        return
    output = text.split(sep)
    if option == "unique":
        output = list(dict.fromkeys(output))
    elif option == "ordered":
        output.sort()
    elif option == "shuffle":
        random.shuffle(output)
    elif option:
        yield ("ERROR")
        return
    for elm in output:
        yield elm
    
if __name__ == '__main__':
    text = "Le Lorem Ipsum simplement est simplement du faux texte. Le Lorem est"
    print ("test")
    for word in generator(text, sep=" "):
        print(word)
    print ("test_shuffle")
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)
    print ("test_unique")
    for word in generator(text, sep=" ", option="unique"):
        print(word)
    print ("test error")
    for word in generator("hello", sep=" ", option="uniqu"):
        print(word)