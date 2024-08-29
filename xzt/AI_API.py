from zhipuai import ZhipuAI
import pandas as pd
client = ZhipuAI(api_key="dac548c212d2a8c8478b153969d2fc67.YzGFEnhMQb1Hird2") # 填写您自己的APIKey
path="E:/PMAIP/xzt/negative_prompt.txt"
path2="E:/PMAIP/xzt//data_AI/txt/slice_1.txt"
# 读取文件内容
with open(path, 'r', encoding='utf-8') as file:
    content = file.read()

with open(path2, 'r', encoding='utf-8') as file:
    content2 = file.read()



# 构建消息
messages = [
    {"role": "assistant", "content": content},
    {"role": "user", "content": content2},
]

# 调用API
response = client.chat.completions.create(
    model="glm-4-0520",  # 填写需要调用的模型编码
    messages=messages,
)

# 打印响应
print(response.choices[0].message)