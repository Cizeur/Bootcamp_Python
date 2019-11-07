class ColorFilter:

    def invert(self, array):
        array[:,:,:] = 1- array[:,:,:]
        return array
    
    def to_blue(self, array):
        array[:,:,:2] = np.zeros((*array.shape[0:2], 2))
        return  array

    def to_green(self, array):
        array[:,:,[0,2]] = array[:,:,[0,2]] * 0
        return  array

    def to_red(self, array):
        green = self.to_green(np.copy(array))
        blue = self.to_blue(np.copy(array))
        array[:,:,:] = array - green - blue
        return  array

    def celluloid(self, array, threshold = 4):
        test = np.linspace(0.0, 1.0, threshold + 1)
        a = 0.0
        for i in test:
            array[:,:,:] = (np.where((array > a) & (array < i) , a , array))
            a = i
        return  array

    def to_grayscale(self, array, filter = "mean"):
        assert filter in ["w", "weighted"] or filter in ["m", "mean"], "invalid filter"
        if filter in ["m", "mean"]:
            temp = np.sum(array, axis = 2)/3
            temp = temp[:,:,None]
            temp = np.broadcast_to(temp, (*temp.shape[:-1], 3))
            array[:,:,:] = temp
        elif filter in ["w", "weighted"]:
            array[:,:,0] = array[:,:,0] * 0.299
            array[:,:,1] = array[:,:,1] * 0.587
            array[:,:,2] = array[:,:,2] * 0.114
            temp = np.sum(array, axis = 2)
            temp = temp[:,:,None]
            temp = np.tile(temp, (1,1,3))
            array[:,:,:] = temp
        return (array)



if __name__ == "__main__":
    from ImageProcessor import ImageProcessor
    import matplotlib.pyplot as plt
    import numpy as np

    columns = 4
    rows = 2
    size = (columns, rows)
    fig=plt.figure(figsize=size)
    imp = ImageProcessor()
    arr = imp.load("../rainbow.png")
    sc = ColorFilter()
    fig.add_subplot(rows, columns, 1)
    plt.axis('off')
    plt.imshow(arr)
    c = np.copy(arr)
    c = sc.invert(c)
    fig.add_subplot(rows, columns, 2)
    plt.axis('off')
    plt.imshow(c)
    c = np.copy(arr)
    sc.to_blue(c)
    fig.add_subplot(rows, columns, 3)
    plt.axis('off')
    plt.imshow(c)
    c = np.copy(arr)
    sc.to_green(c)
    fig.add_subplot(rows, columns, 4)
    plt.axis('off')
    plt.imshow(c)
    c = np.copy(arr)
    sc.to_red(c)
    fig.add_subplot(rows, columns, 5)
    plt.axis('off')
    plt.imshow(c)
    c = np.copy(arr)
    sc.celluloid(c, 6)
    fig.add_subplot(rows, columns, 6)
    plt.axis('off')
    plt.imshow(c)
    c = np.copy(arr)
    sc.to_grayscale(c, "m")
    fig.add_subplot(rows, columns, 7)
    plt.axis('off')
    plt.imshow(c)
    c = np.copy(arr)
    sc.to_grayscale(c, "w")
    fig.add_subplot(rows, columns, 8)
    plt.axis('off')
    plt.imshow(c)
    plt.show()
