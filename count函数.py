"""
统计重复条目 20170223  144120行数据耗时42min
"""
import pandas as pd
import csv

import time

# 开始时间
start = time.clock()
# 统计重复项目
csv_reader = csv.reader(open('F:\ChinaVis\\20170223.csv', encoding='utf-8'))
csv_reader = (list(csv_reader))
l = []
i = 0
for row in csv_reader[1:]:
    b = csv_reader.count(row)
    i = i + 1
    print(i, b)
    l.append(b)

data = pd.read_csv('F:\ChinaVis\\20170223.csv')
datacount = pd.DataFrame(l, columns=['count'])

data = pd.concat([data, datacount], axis=1)
data.to_csv('F:\ChinaVis\\20170223test_tagcount.csv', index=False, encoding='utf_8_sig')

# 结束时间
elapsed = (time.clock() - start)
print("Test Time used:", int(elapsed / 60), "min")
