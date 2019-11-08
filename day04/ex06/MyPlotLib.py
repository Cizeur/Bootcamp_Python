import matplotlib.pyplot as plt

class MyPlotLib():
    def histogram(self, data, features):
        df = data[features].T
        df.dropna()
        print (df)
        hist = df.hist()
        plt.hist(hist)
        df = pd.DataFrame({
            'length': [1.5, 0.5, 1.2, 0.9, 3],
            'width': [0.7, 0.2, 0.15, 0.2, 1.1]
        }, index= ['pig', 'rabbit', 'duck', 'chicken', 'horse'])
        hist = df.hist()
        plt.hist(hist)
        plt.show()



if __name__ == "__main__":
    from FileLoader import FileLoader
    loader = FileLoader()
    data = loader.load("../ressources/athlete_events.csv")
    c = MyPlotLib()
    c.histogram(data, ["Height", "Weight"])