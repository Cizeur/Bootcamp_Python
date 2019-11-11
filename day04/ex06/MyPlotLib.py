import matplotlib.pyplot as plt
import pandas as pd


class MyPlotLib():

    def histogram(self, data, features, bins=10):
        df = data[features]
        df.hist(bins=bins)

    def density(self, data, features):
        df = data[features]
        df.plot.kde()

    def pair_plot(self, data, features):
        df = data[features]
        pd.plotting.scatter_matrix(df)

    def box_plot(self, data, features):
        df = data[features]
        df.plot.box()


if __name__ == "__main__":
    from FileLoader import FileLoader
    loader = FileLoader()
    data = loader.load("../ressources/athlete_events.csv")
    features = ["Weight", "Height", "Age"]
    c = MyPlotLib()
    data.drop_duplicates(subset="Name", inplace=True)
    data.drop_duplicates(subset="ID", inplace=True)
    c.histogram(data, features)
    c.density(data, features)
    c.pair_plot(data, features)
    c.box_plot(data, features)
    plt.show()
