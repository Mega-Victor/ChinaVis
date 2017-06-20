"""
筛选时间戳
"""
import pandas as pd
import time

# 开始时间
start = time.clock()

data = pd.read_csv('F:\ChinaVis/20170223_tag_count_dist.csv')
print(data.ix[data.conntime>1487779200].info())



# 结束时间
elapsed = (time.clock() - start)
print("Test Time used:", int(elapsed), "s")
