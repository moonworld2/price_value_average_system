"""

作者：moonw
日期：2022年05月06日

"""
import csv
import pandas as pd
from setting import Settings


class Average:
    def __init__(self):
        self.settings = Settings()
        filename = self.settings.filename

        data_frame = pd.read_csv(filename)
        total_price = data_frame['金额'].str.replace(',', '').astype(int)
        value = data_frame['总手'].str.replace(',', '').astype(int)

        self.sum_value=sum(value)
        self.sum_total_price=sum(total_price)
        self.average = self.sum_total_price/ self.sum_value
        self.average = round(self.average, 2)
