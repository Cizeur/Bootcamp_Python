def youngestFellah(df, o_year):
    df = df[['ID','Name','Sex', 'Year', 'Age']]
    df = df.drop(df[df.Year != o_year ].index)
    f = df.groupby(['Sex'])['Age'].min()
    print (f.to_dict())
    return (df)

if __name__ == "__main__":
    from FileLoader import FileLoader
    loader = FileLoader()
    data = loader.load("../ressources/athlete_events.csv")
    youngestFellah(data, 2004)
