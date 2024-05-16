# -*- coding: utf-8 -*-
"""
sorted排序
"""

# 定義一個包含分數的列表
score = [99, 89, 92, 100, 62, 73]

# 將分數列表進行排序，並將排序後的結果存儲在另一個變量 data 中
data = sorted(score)

# 打印原始的分數列表
print('原本的資料:', score)

# 打印排序後的分數列表
print('排序後的資料:', data)

# 使用 sorted() 函數對 score 列表進行排序，並以reverse降序方式打印結果
print(sorted(score,reverse=True))

for i in sorted(score,reverse=True):
    print(i)