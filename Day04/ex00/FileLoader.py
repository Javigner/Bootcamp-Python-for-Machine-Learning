import pandas as pd

class Filerloader:
    def load(path):
        df = pd.read_csv(path)
        size = df.shape
        print("Loading dataset of dimensions " + str(size[0]) + ' x ' + str(size[1]))
        return df
    def display(df, n):
        if n >= 0:
            print (df.head(n))
        if n < 0:
            print(df.tail(-n))
            

df = Filerloader.load("FL_insurance_sample.csv")
Filerloader.display(df, 0)
