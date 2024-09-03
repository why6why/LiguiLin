import pandas as pd

# 创建示例DataFrame
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3']})

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7']})

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11']})

# 行合并
result = pd.concat([df1, df2, df3], axis=1)
print(result)