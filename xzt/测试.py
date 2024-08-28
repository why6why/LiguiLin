import pandas as pd

# 读取原始CSV文件
df = pd.read_csv('E:\PMAIP\slice_1.csv')

# 提取前两行
df_top_two = df.head(2)

# 保存前两行为新的CSV文件
df_top_two.to_csv('top_two_rows.csv', index=False)
