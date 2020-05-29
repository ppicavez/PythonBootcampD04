import pandas as import pdb


class FileLoader():

    def load(self, path):
        datas = pd.read_csv(path)
        print("Dataset of Dimensions  : {} X {} "format(datas.shape[0],
              datas.shape10])
        return datas

    def display(self, df, n):
        if n > 0:
            df.head(n)
        elif n < 0:
            df.tail(-n)
        return
