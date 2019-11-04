

t = (19, 42, 21)

if isinstance(t, tuple):
    if len(t) == 1:
        print("The 1 number is: %i" % (t))
    else:
        try:
            t = list(map(int, t))
            string = list(map(str, t))
        except Exception:
            print("Integers only")
            exit(1)
        string = ", ".join(string)
        print("The %d numbers are: %s" % (len(t), string))
else:
    print("Not a tuple")
