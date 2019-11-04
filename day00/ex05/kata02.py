

t = (3, 30, 2019, 9, 25)


if isinstance(t, tuple):
    if len(t) != 5:
        print("Tuple of 5 int needed")
    else:
        try:
            nb = tuple(map(int, t))
            print("{3:02d}/{4:02d}/{2:04d} {0:02d}:{1:02d}".format(*t))
        except Exception:
            print("Tuple of int please")
else:
    print("Not a tuple")
