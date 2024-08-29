import pandas as pd

# 读取原始CSV文件
df = pd.read_csv('E:/PMAIP/xzt/data_AI/top_two_rows.csv')

# # 提取前两行
# df_top_two = df.head(2)

# 保存前两行为新的CSV文件
print(df)
