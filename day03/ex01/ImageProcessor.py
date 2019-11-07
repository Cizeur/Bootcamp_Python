import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np


class ImageProcessor():

    def load(self, path):
        arr = mpimg.imread(path)
        print("Loading image of dimensions {} x {}".format(
            (*(arr.shape[0:2]))))
        arr = arr[:,:,:3]
        return arr

    def display(self, array):
        plt.imshow(array)
        plt.show()


if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load("../42AI.png")
    print(arr)
    imp.display(arr)
