
t = (0, 4, 132.42222, 10000, 12345.67)


if isinstance(t, tuple):
    if len(t) < 2:
        print("Tuple of at least two needed")
    else:
        try:
            print("day_{0:02d}, ex_{1:02d} : ".format(*t), end='')
        except Exception:
            print("Error: Int only for first two elems")
            exit(1)
    if len(t) > 2:
        try:
            string = ", ".join(map("{:.2e}".format, t[2:]))
            print(string, end='')
        except Exception:
            print("Error numbers only expected", end='')
    print("")
else:
    print("Error: not a tuple")
