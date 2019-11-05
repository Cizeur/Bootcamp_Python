from time import sleep
import time
import sys


def ft_progress(mylist: list):
    length = len(mylist)
    start = time.time()
    eta = 0
    updated = 0
    if length:
        for key, val in enumerate(mylist):
            key += 1
            current = time.time()-start
            percent = key * 100 // length
            avancement = percent // 5 * "=" + ">"
            if not (percent % 5) and updated:
                eta = current * 100 / percent
                updated = 0
            if percent % 5:
                updated = 1
            print("{: <80s}\r".format(" "), end="")
            print("ETA:{:.2f}s [{:3d}%] [{:21s}]"
                  "{:d}/{: d} |elapsed time {:.2f}s\r"
                  .format(eta, percent, avancement, key, length, current),
                  end="")
            yield val
        print("")
