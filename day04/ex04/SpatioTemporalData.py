class SpatioTemporalData():

    def __init__(self, data):
        self._data = data

    def where(self, year):
        df = self._data
        df = df.drop(df[df.Year != year].index)
        df.drop_duplicates(subset="City", inplace=True)
        return (df["City"].tolist())

    def when(self, location):
        df = self._data
        df = df.drop(df[df["City"] != location].index)
        df.drop_duplicates(subset="Year", inplace=True)
        return (df["Year"].tolist())


if __name__ == "__main__":
    from FileLoader import FileLoader
    loader = FileLoader()
    data = loader.load("../ressources/athlete_events.csv")
    sp = SpatioTemporalData(data)
    print(sp.where(1896))
    print(sp.where(2016))
    print(sp.when('Athina'))
    print(sp.when('Paris'))
