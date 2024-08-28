import os
import pandas as pd
import requests
import json
path="C:/Users/Administrator/Desktop/"
##读取excel文件，第一行作为数据而不是列名，若第一行是列名，去掉header=None
df=pd.read_excel(path+'贵阳恒大群聊-新.xlsx',header=None)#读取excel数据
# #生成csv文件的数量
# num_slices=(len(df)+9)//10

# #数据切片（示例：按100条信息进行切片）
# for i in range(num_slices):
#     start=i*10
#     end=start+10
#     slice_df=df[start:end]
#     slice_df.to_csv(f'slice_{i+1}.csv',index=False,header=False)
# print(slices[0])

 
 
 # 初始化一个空的DataFrame，用于存储合并后的数据
merged_df = pd.DataFrame()

# 每次处理10行数据
for i in range(0, len(df), 10):
    # 获取切片
    slice_df = df[i:i+10]
    # 将切片的每一行合并成一行，用逗号分隔
    merged_row = ','.join(slice_df.iloc[:, 0].astype(str))
    # 将合并后的行添加到新的DataFrame中
    merged_df = merged_df.append([merged_row], ignore_index=True)

# 将合并后的DataFrame保存为CSV文件
merged_df.to_csv('merged_data.csv', index=False, header=False)
 
 