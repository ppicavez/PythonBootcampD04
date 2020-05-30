import pandas as pd


class SpatioTemporalData():

    def __init__(self, dataset):
        self.datas = dataset

    def when(self, location):
        result = self.datas
        mask = (result["City"] == location)
        result = self.datas[mask]
        result = result.drop_duplicates(subset=['Year'])

        result = result['Year'].values
        my_list = result.tolist()

        return my_list

    def where(self, date):
        result = self.datas
        mask = (result["Year"] == date)
        result = self.datas[mask]
        result = result.drop_duplicates(subset=['City'])

        result = result['City'].values
        my_list = result.tolist()

        return my_list
