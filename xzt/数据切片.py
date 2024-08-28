import os
import pandas as pd
import requests
import json
path="C:/Users/Administrator/Desktop/"
##读取excel文件，第一行作为数据而不是列名，若第一行是列名，去掉header=None
df=pd.read_excel(path+'贵阳恒大群聊-新.xlsx',header=None)#读取excel数据
#生成csv文件的数量
num_slices=(len(df)+9)//10

#数据切片（示例：按100条信息进行切片）
for i in range(num_slices):
    start=i*10
    end=start+10
    slice_df=df[start:end]
    slice_df.to_csv(f'slice_{i+1}.csv',index=False,header=False)
# print(slices[0])

 
 
 
 
 