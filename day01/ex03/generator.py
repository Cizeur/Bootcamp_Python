def custom_sort(string):
    return(string.swapcase())


def generator(text, sep="", option=None):
    """Option is an optional arg, sep is mandatory"""
    if not isinstance(text, str):
        yield("ERROR")
        return
    if not isinstance(sep, str) or not sep:
        yield("ERROR")
        return
    output = text.split(sep)
    if option == "unique":
        output = list(dict.fromkeys(output))
    elif option == "ordered":
        output.sort(key=custom_sort)
    elif option == "shuffle":
        i = 1
        while i <= 10:
            stock = output
            output = [x for i, x in enumerate(stock) if i % 2]
            output += [x for i, x in enumerate(stock) if not i % 2]
            i += 1
    elif option:
        yield("ERROR")
        return
    for elm in output:
        yield elm


if __name__ == '__main__':
    text = "Le Lorem Ipsum est simplement du faux texte."\
          + "Le Lorem est une base de simplemet"
    #  text = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18"
    print("######test######")
    for word in generator(text, sep=" "):
        print(word)
    print("######test_shuffle######")
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)
    print("######test_ordered######")
    for word in generator(text, sep=" ", option="ordered"):
        print(word)
    print("######test_unique######")
    for word in generator(text, sep=" ", option="unique"):
        print(word)
    print("######test error######")
    for word in generator("hello", sep=" ", option="uniqu"):
        print(word)
