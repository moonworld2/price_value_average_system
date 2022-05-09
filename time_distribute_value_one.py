"""

作者：moonw
日期：2022年05月06日

"""
from setting import Settings as set
from average import Average as ave
import matplotlib.pyplot as plt
import pandas as pd

Average=ave()
average=Average.average
sum_value=Average.sum_value

setting=set()
filename=setting.filename

data_frames=pd.read_csv(filename)
price_list=(data_frames['开盘']+data_frames['收盘'])/2  # 计算1分钟内均价
value_list=data_frames['总手'].str.replace(',','').astype(int)  # 统计总手数（列表形式）
number=len(price_list)  # 统计数目条
number_list=list(range(1,number+1))  # 形成数目列表
average_list=[]
for index in number_list:
    average_list.append(average)  # 形成当日均值线



fig,ax1=plt.subplots(figsize=(15,9)) # 调节图片大小
plt.xticks(rotation=45)  # x轴倾斜45度

ax1.bar(x=number_list,height=value_list,width=0.6)
ax1.set_xlabel("time")
ax1.set_ylabel('value')
ax1.set_title(f'{setting.date}-minutue \n average({average}) sum value({sum_value})')

ax2 = ax1.twinx()  # 双坐标关键
ax2.plot(number_list,price_list,color='red')
ax2.plot(number_list,average_list,color='green')
ax2.set_ylabel('price')

plt.savefig(f'C:/Users/moonw/Desktop/股票分析图/{setting.stockID}/{setting.date}-minutue.png',bbox_inches='tight')
plt.show()

print(setting.date)
print(average)
print(sum_value)
print(data_frames['时间'][0])