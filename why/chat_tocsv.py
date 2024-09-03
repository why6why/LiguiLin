import requests
import pandas as pd
import os
import json
from datetime import datetime

path="F:/Working/PMAIP/xzt/positive_prompt.txt"
folder_path="F:/Working/PMAIP/xzt//data_AI/txt"
infile_contents = []# 文件内容数组
content_o = []#origin
content_n = []#negative
content_p = []#positive

print("start:",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 读取文件内容
with open(path, 'r', encoding='utf-8') as file:
    prompts = file.read()

# 遍历文件夹中的所有文件
# for filename in os.listdir(folder_path):
for i in range(1,30):
    # 构建完整的文件路径
    file_path = os.path.join(folder_path, 'slice_'+str(i)+'.txt')
    # 打开并读取文件内容
    # print(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        content_o_ = file.read()
        content_o.append(content_o_)
content_p = pd.read_csv('F:/Working/PMAIP/why/datasets/sentiment_result_positive.csv')
content_n = pd.read_csv('F:/Working/PMAIP/why/datasets/sentiment_result_negative.csv')
# content_n_ = pd.read_csv('sentiment_result_negative.csv')
content_o = pd.DataFrame(content_o)
result = pd.concat([content_o, content_p, content_n], axis=1)
# result.to_csv('why/datasets/sentiment_result_all.csv',index=False,encoding='utf8')#不要索引号

excel_writer = pd.ExcelWriter('F:/Working/PMAIP/why/datasets/output.xlsx', engine='xlsxwriter')  # 创建一个Excel写入器
result.to_excel(excel_writer, sheet_name='Sheet1', index=False)  # 将DataFrame写入到Excel文件中，不包含索引
excel_writer.save()  # 保存Excel文件
