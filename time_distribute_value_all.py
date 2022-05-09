"""

作者：moonw
日期：2022年05月08日

"""
import glob
import os.path
import pandas as pd
import matplotlib.pyplot as plt
from setting import Settings as set




def File_name(input_file):
    name = os.path.basename(input_file)
    namelist = name.split('.', 1)
    return namelist[0]

def Date_str(filename):
    list=filename.split('_',1)
    return list[0]


def Average_TotalValue_TotalPrice(filename):  # 返回两个参数
    address = f"E:/python/price_value_average_system/data/{settings.stockID}/{filename}.csv"
    data_frame = pd.read_csv(address)
    total_price = data_frame['金额'].str.replace(',', '').astype(int)
    value = data_frame['总手'].str.replace(',', '').astype(int)
    sum_value = sum(value)
    sum_total_price = sum(total_price)
    average = sum_total_price / sum_value
    average = round(average, 2)
    return average, sum_value


settings = set()
inputPath = f'E:/python/price_value_average_system/data/{settings.stockID}'  # 原数据文件夹所在地址

statis_filename=f'C:/Users/moonw/Desktop/股票分析图/{settings.stockID}/{settings.stockID}_stais.csv'  # 统计表储存地址
with open(statis_filename,'w') as f:
    f.write(settings.first_line)
f.close()

for input_file in glob.glob(os.path.join(inputPath, '*.csv')):
    filename = File_name(input_file)
    DataList = Average_TotalValue_TotalPrice(filename)  # 返回两个参数 分别为均值，总数，

    address = f"E:/python/price_value_average_system/data/{settings.stockID}/{filename}.csv"  # 文件路径
    data_frames = pd.read_csv(address)
    price_list = (data_frames['开盘'] + data_frames['收盘']) / 2  # 计算1分钟内均价
    value_list = data_frames['总手'].str.replace(',', '').astype(int)  # 统计总手数（列表形式）
    number = len(price_list)  # 统计数目条
    number_list = list(range(1, number + 1))  # 形成数目列表
    average_list = []
    for index in number_list:
        average_list.append(DataList[0])  # 形成当日均值线

# 形成统计表
    with open(statis_filename,'a') as f:
        date_str=str(Date_str(filename))
        average_str=str(DataList[0])
        value_str=str(DataList[1])
        statis_data_str=date_str+','+average_str+','+value_str+'\n'
        f.write(statis_data_str)
    f.close()

# 形成图片
    fig, ax1 = plt.subplots(figsize=(15,9))
    plt.xticks(rotation=45)  # x轴倾斜45度

    ax1.bar(x=number_list, height=value_list, width=0.6)
    ax1.set_xlabel("time")
    ax1.set_ylabel('value')
    ax1.set_title(f'{filename} \n average({DataList[0]}) sum value({DataList[1]})')

    ax2 = ax1.twinx()  # 双坐标关键
    ax2.plot(number_list, price_list, color='red')
    ax2.plot(number_list, average_list, color='green')
    ax2.set_ylabel('price')

    plt.savefig(f'C:/Users/moonw/Desktop/股票分析图/{settings.stockID}/{filename}.png',bbox_inches='tight')
    # 图片储存地址 bbox_inches='tight'表示裁剪多余空白
    plt.close()


