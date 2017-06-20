import pandas as pd
# import jieba
import os
import time


def getHour(time):
    return time.tm_hour


def getMonth(time):
    return time.tm_mon


def getDay(time):
    return time.tm_mday


def getMin(time):
    return int(time.tm_min / 10)

def MaxMinNormalization(x,Max,Min):
    x = (x - Min) / (Max - Min);
    return x


l = []
for day in range(54,61):#   ###############修改   1111111
    df = pd.read_csv('F:\ChinaVis/allData/data_labeled/%d.csv' %day, sep=',')
    df['recidt'] = (df.recitime / 1000).apply(time.localtime)
    df['hour'] = df['recidt'].apply(getHour)
    df['month'] = df['recidt'].apply(getMonth)
    df['day'] = df['recidt'].apply(getDay)
    for i in range(0,24):
        hour_list = df[df['hour']==i]['hour'].tolist()
        b = hour_list.count(i) #0-23每小时短信数量
        l.append(b)
print(l)
heatmap_count = []
for days in range(54, 61):   ###########修改    2222222
    df1 = pd.read_csv('F:\ChinaVis/allData/data_labeled/%d.csv' % days, sep=',')
    df1['recidt'] = (df1.recitime / 1000).apply(time.localtime)
    df1['hour'] = df1['recidt'].apply(getHour)
    df1['month'] = df1['recidt'].apply(getMonth)
    df1['day'] = df1['recidt'].apply(getDay)
    max_count=max(l)
    min_count=min(l)
    for hour in range(0,24):
        h_type = df1[df1['hour'] == hour]['hour'].tolist()
        c = h_type.count(hour)
        normal=MaxMinNormalization(c,max_count,min_count)*100
        heatmap_count.append(str('['+str(days-54)+','+str(hour)+','+str('%d' % normal)+']'+','))
                ###修改   33333333

f = open('F:\heatmap/4.17-4.23.txt', 'w')    ##   修改    44444444
for i in heatmap_count:
    f.write(i)
f.close()





# df['hour'].to_excel('F:\ChinaVis/allData\data_date_count/0223.xlsx')
# for i in range(0, 24):
#     for j in range(0, 6):
#         index = i * 6 + j
#         filename = 'F:/%d.txt' % index
#         wfile = open(filename, 'w')
#         print(i, j, index)
#         df_temp = df[df['hour'] == i]
#         counts = df_temp[df_temp['min'] == j]['lonlat'].value_counts()
#         for k in range(0, len(counts)):
#             # print('%s,%d'%(hour.index[i],hour[i]))
#             wfile.write(counts.index[k] + ',' + str(counts[k]) + '\n')
