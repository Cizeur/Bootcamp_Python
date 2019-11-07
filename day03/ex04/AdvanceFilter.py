import numpy as np

# require 42ai module check day 02 ex04 or just remove ft_progress and log
from ai42.progressbar import ft_progress
from ai42.logging.log import log


class AdvancedFilter():
    MEAN_FILTER = np.full((3, 3), 1.0)
    GAUSS_FILTER = np.asarray([[1, 2, 1], [2, 4, 2], [1, 2, 1]])

    @log
    def apply_filter(self, array, filter):
        assert filter.shape[0] == filter.shape[1], "please square filter"
        result = array.copy()
        ks = filter.shape[0]
        linelen = result.shape[1] - ks + 1
        for ind in ft_progress(range((array.shape[0] - ks + 1) * linelen)):
            i = ind // linelen
            j = ind % linelen
            for k in range(3):
                result[i, j, k] = np.sum(np.multiply(
                    filter, array[i: i+ks, j: j + ks, k])) / np.sum(filter)
            ind += 1
        print(ind)
        result = result[:-ks + 1, : -ks + 1, :]
        print(result.shape)
        return result

    def mean_blur(self, array):
        return self.apply_filter(array, self.MEAN_FILTER)

    def gaussian_blur(self, array):
        return self.apply_filter(array, self.GAUSS_FILTER)


if __name__ == "__main__":
    from ImageProcessor import ImageProcessor
    import matplotlib.pyplot as plt
    import numpy as np

    columns = 3
    rows = 1
    size = (columns, rows)
    fig = plt.figure(figsize=size)

    imp = ImageProcessor()
    arr = imp.load("../rainbow.png")
    af = AdvancedFilter()
    print(arr.shape)

    fig.add_subplot(rows, columns, 1)
    plt.axis('off')
    plt.imshow(arr)

    c = af.mean_blur(arr)
    fig.add_subplot(rows, columns, 2)
    plt.axis('off')
    plt.imshow(c)

    c = af.gaussian_blur(arr)
    fig.add_subplot(rows, columns, 3)
    plt.axis('off')
    plt.imshow(c)
    plt.show()
