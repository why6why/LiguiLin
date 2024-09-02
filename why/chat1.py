import requests
import pandas as pd
import os
import json

path="F:/Working/PMAIP/xzt/negative_prompt.txt"
folder_path="F:/Working/PMAIP/xzt//data_AI/txt"
infile_contents = []#文件内容数组
# 读取文件内容
with open(path, 'r', encoding='utf-8') as file:
    prompts = file.read()

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):

    # 构建完整的文件路径
    file_path = os.path.join(folder_path, filename)
    # 打开并读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # file_contents.append(content)

    # 设置大模型请求参数
    messages = [
            {
                "role": "system",
                "content": prompts
            },
            {
                "role": "user",
                "content": content
            }
        ]
    url = "https://aiapi.jinbizhihui.com:20000/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer your_token"
    }
    payload = {
        "model": "cele/Cele-72B-Chat-GPTQ-Int4",
        "messages":messages,
        "temperature": 0.1
    }

    #将数据传入模型
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        # 在这里处理返回的数据，可以根据需要提取具体的字段或执行相应的操作
        # print(data["choices"][0]['message']['content'])

        # 将JSON对象写入文件

        infile_contents.append(data["choices"][0]['message']['content'])
        # if(len(infile_contents) == 3):
        #     break
        print(len(infile_contents))
    else:
        print("请求失败，错误码：", response.status_code)

# # 将所有结果保存到json中
# sentiment_result = "why/datasets/sentiment_result.json"
# with open(sentiment_result, 'w', encoding='utf-8') as file:
#     # 确保JSON数据是格式化的，并且使用utf-8编码
#     json.dump(infile_contents, file, ensure_ascii=False, indent=4)

# 将所有结果保存到csv中
df = pd.DataFrame(infile_contents)#格式转换
df.to_csv('why/datasets/sentiment_result.csv',index=False,encoding='utf8')#不要索引号