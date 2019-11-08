def proportionBySport(df, o_year, sport, gender):
    df = df[['ID','Name','Sex', 'Year', 'Sport']]
    df = df.drop(df[df.Sex != "F" ].index)
    df = df.drop(df[df.Year != o_year ].index)
    df.drop_duplicates(subset ="ID", inplace = True)
    total = df.shape[0]
    df = df.drop(df[df.Sport != sport ].index)
    print (df.shape[0]/total)
    return (df)

if __name__ == "__main__":
    from FileLoader import FileLoader
    loader = FileLoader()
    data = loader.load("../ressources/athlete_events.csv")
    proportionBySport(data, 2004, 'Tennis', 'F')
