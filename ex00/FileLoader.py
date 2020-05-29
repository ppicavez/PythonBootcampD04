import pandas as pd


class FileLoader():

    def load(self, path):
        datas = pd.read_csv(path)
        print("Dataset of Dimensions  : {} X {} ".format(datas.shape[0],
              datas.shape[1]))
        return datas

    def display(self, df, n):
        if n > 0:
            return df.head(n)
        elif n < 0:
            return df.tail(-n)
        
