import matplotlib.pyplot as plt
import pandas as pd


class Komparator():
    data = None

    def __init__(self, data):
        self.data = data

    def compare_box_plots(self, categorical_var, numerical_var):
        df = self.data
        fig, axs = plt.subplots(len(categorical_var),
                                len(numerical_var), squeeze=False)
        for j, cat in enumerate(categorical_var):
            for i, num in enumerate(numerical_var):
                ax = axs[j, i]
                ax.set_xlabel(num)
                for val in df[cat].unique():
                    if num == float('nan'):
                        continue
                    a = df.drop(df[df[cat] != val].index)
                    if not a.empty:
                        df.boxplot(column=num, by=cat, ax=ax)
        fig.suptitle("")

    def density(self, categorical_var, numerical_var):
        df = self.data
        fig, axs = plt.subplots(len(categorical_var),
                                len(numerical_var), squeeze=False)
        for j, cat in enumerate(categorical_var):
            for i, num in enumerate(numerical_var):
                ax = axs[j, i]
                ax.set_xlabel(num)
                for val in df[cat].unique():
                    if num == float('nan'):
                        continue
                    a = df.drop(df[df[cat] != val].index)
                    if not a.empty:
                        a[num].plot(kind="kde", ax=ax, label=val)
            ax.legend()

    def compare_histograms(self, categorical_var, numerical_var):
        df = self.data
        plt.style.use('seaborn-deep')
        fig, axs = plt.subplots(len(categorical_var),
                                len(numerical_var), squeeze=False)
        for j, cat in enumerate(categorical_var):
            for i, num in enumerate(numerical_var):
                ax = axs[j, i]
                ax.set_xlabel(num)
                plt.sca(ax)
                tot = []
                labls = []
                for val in df[cat].unique():
                    a = df.drop(df[df[cat] != val].index)
                    if not a.empty:
                        tot.append(a[num])
                        labls.append(val)
                plt.hist(tot, label=labls)
            ax.legend()


if __name__ == "__main__":
    from FileLoader import FileLoader
    loader = FileLoader()
    data = loader.load("../ressources/athlete_events.csv")
    features = ["Weight", "Height", "Age"]
    c = Komparator(data)
    data.drop_duplicates(subset="Name", inplace=True)
    data.drop_duplicates(subset="ID", inplace=True)
    c.compare_box_plots(["Medal", "Sex"], features)
    c.density(["Medal", "Sex"], features)
    c.compare_histograms(["Medal", "Sex"], features)
    plt.show()
