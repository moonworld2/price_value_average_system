"""

作者：moonw
日期：2022年05月06日

"""
class Settings:

    def __init__(self):
        # 股票代码
        self.stockID = 300750

        # 使用单个生成程序 time_distribute_value_one 用的参数
        self.date=20220422
        self.filename = f"data/{self.stockID}/{self.date}_minute.csv"

        # time_distribute_value_all 用的参数
        self.first_line='日期,实际均值,成交总数,均*成,sum(e),totlal_average,目标差值,差值变化速率,复盘差值'
