import numpy as np

def howManyMedals(df, name):
    df = df[['Name', 'Year', 'Medal']]
    df = df.drop(df[df.Name != name ].index)
    df = df.dropna()
    df.insert(2, "G", 0, True)
    df.insert(2, "B", 0, True)
    df.insert(2, "S", 0, True)
    df["B"] = [1 if x == "Bronze" else 0 for x in df["Medal"]]
    df["S"] = [1 if x == "Silver" else 0 for x in df["Medal"]]
    df["G"] = [1 if x == "Gold" else 0 for x in df["Medal"]]
    df = df.groupby(['Year']).agg({'G':'sum','S':'sum','B':'sum'})
    return (df.T.to_dict())

if __name__ == "__main__":
    from FileLoader import FileLoader
    loader = FileLoader()
    data = loader.load("../ressources/athlete_events.csv")
    print(howManyMedals(data, 'Kjetil Andr Aamodt'))
