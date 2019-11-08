import pandas


class FileLoader():

    def load(self, path):
        try:
            data = pandas.read_csv(path)
            print("Loading dataset of dimensions {} x {}".format(*data.shape))
            return(data)
        except:
            raise Exception("Invalid File")
        return None

    def display(self, df, n):
        print(df[:n] if n >= 0 else df[n:])


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load("../ressources/athlete_events.csv")
    loader.display(data, 12)
    loader.display(data, -12)
