import numpy as np

class ScrapBooker():
    def crop(self, array, dimensions, position = (0,0)):
        assert dimensions[0] <= array.shape[0], "Crop height bigger than image"
        assert dimensions[1] <= array.shape[1], "Crop width bigger than image"
        assert dimensions[0] >= 0 or dimensions[1] >= 0, "Dimensions need to be positive"
        return array[position[0]: dimensions[0] + position[0],
        position[1]: dimensions[1] + position[1]]

    def thin(self, array, n, axis = 0):
        return np.delete(array, np.s_[::n], axis)

    def juxtapose(self, array, n, axis = 0):
        return np.concatenate([array] * n , axis)

    def mosaic(self, array, dimensions):
        tupl=(*dimensions, 1,1,1)
        return np.tile(array, tupl)
        

if __name__ == "__main__":
    from ImageProcessor import ImageProcessor
    import matplotlib.pyplot as plt

    columns = 4
    rows = 2
    fig=plt.figure(figsize=(4, 2))
    imp = ImageProcessor()
    arr = imp.load("./42AI.png")
    sc = ScrapBooker()
    fig.add_subplot(rows, columns, 1)
    plt.imshow(arr)
    fig.add_subplot(rows, columns, 2)
    c = sc.crop(arr, (100, 100), (30,30))
    print (c.shape)
    plt.imshow(c)
    fig.add_subplot(rows, columns, 3)
    c = sc.thin(arr, 2, 0)
    plt.imshow(c)
    fig.add_subplot(rows, columns, 4)
    c = sc.thin(arr, 2, 1)
    plt.imshow(c)
    fig.add_subplot(rows, columns, 5)
    c = sc.juxtapose(arr, 4)
    plt.imshow(c)
    fig.add_subplot(rows, columns, 6)
    c = sc.juxtapose(arr, 4, 1)
    plt.imshow(c)
    fig.add_subplot(rows, columns, 8)
    c = sc.mosaic(arr, (2 , 3))
    print(c.shape)
    c = np.concatenate(np.concatenate(c,1), 1)
    plt.imshow(c)
    plt.show()

    