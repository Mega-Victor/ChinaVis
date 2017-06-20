"""
合并两个具有同样标签的数据
"""
import pandas as pd
import time

# 开始时间
start = time.clock()


for day in range(10,27):
    path1='F:\ChinaVis/allData/data/201704%d.csv' %day
    path2='F:\ChinaVis/allData/data_add_city_dist_type/201704%d.csv'%day
    df1 = pd.read_csv(path1, sep=',')
    df2 = pd.read_csv(path2, sep=',')
    df2 = df2.loc[:,['type','city','dist']]


    df_merge = pd.merge(df1, df2, how='left',left_index=True,right_index=True)

    df_merge.to_csv('F:\ChinaVis/allData/data_labeled/201704%d_labeled.csv' %day, index=False)

# 结束时间
elapsed = (time.clock() - start)
print("Test Time used:", int(elapsed/60), "min")
