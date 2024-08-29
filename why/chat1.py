import requests
url = "https://aiapi.jinbizhihui.com:20000/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer your_token"
}
payload = {
    "model": "cele/Cele-72B-Chat-GPTQ-Int4",
    "messages": [
        {
            "role": "system",
            "content": "你是一个商品类目预测专家，对输入的内容，进行商品类目预测，类目包含'大家电、全屋家具、营养保健、茶饮冲调、休闲零食、生鲜水果、肉禽蛋品、粮油调味、中外名酒、家居用品、当地玩乐、旅游酒店、智能锁、华帝电器专场、生活电器、厨房电器、空调'。返回商品的分类。如果返回的类目不在包含的内容中，返回'明星单品'四字"
        },
        {
            "role": "user",
            "content": "三只松鼠"
        }
    ],
    "temperature": 0.1
}
response = requests.post(url, headers=headers, json=payload)
if response.status_code == 200:
    data = response.json()
    # 在这里处理返回的数据，可以根据需要提取具体的字段或执行相应的操作
    print(data)
else:
    print("请求失败，错误码：", response.status_code)