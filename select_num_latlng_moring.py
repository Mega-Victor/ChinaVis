import pandas as pd
import numpy as np

import time
import matplotlib.pyplot as plt
start = time.clock()
df_phone = pd.read_csv('F:\ChinaVis/phoneNum.txt',sep='\n')
df_list = df_phone.values
for item in df_list:
    phone = str(item[0])
    phoneSearch = phone

    df = pd.read_csv('F:\ChinaVis/allData/data/20170417.csv', sep=',')
    df =df.ix[(df.recitime/1000) < 1492401600]
    df =df.ix[(df.conntime/1000) < 1492401600] # before 12:30

    df['diff'] = (df['recitime'] - df['conntime']) / 1000
    df = df[df['diff'] > 0]  # filter recitime<conntime
    df = df[df['diff'] < 3600]  # filter recitime-conntime>half hour  about 97121 left
    df = df[df['phone'].astype(str)== phoneSearch]
    def getHour(time):
        return time.tm_hour
    def getMonth(time):
        return time.tm_mon
    def getDay(time):
        return time.tm_mday
    def getMin(time):
        return int(time.tm_min / 10)


    df['lonlat'] = df['lng'].astype(str) + ',' + df['lat'].astype(str)
    df['recidt'] = (df.recitime / 1000).apply(time.localtime)
    df['hour'] = df['recidt'].apply(getHour)
    df['month'] = df['recidt'].apply(getMonth)
    df['day'] = df['recidt'].apply(getDay)
    df['min'] = df['recidt'].apply(getMin)


    def getCenter(counts):
        if (len(counts) == 0):
            center = '0,0'
        else:
            lngSum = 0
            latSum = 0
            heatSum = 0
            for k in range(0, len(counts)):
                heatSum += counts[k]
            for k in range(0, len(counts)):
                lnglat = counts.index[k].split(',')
                lngSum += float(lnglat[0]) * counts[k] / heatSum
                latSum += float(lnglat[1]) * counts[k] / heatSum
            center = '%.4f,%.4f' % (lngSum, latSum)
        return center


    filename = 'F:/ChinaVis/trace_phone/0417_1/trace-%s.txt' % phoneSearch
    wfile = open(filename, 'w')
    for i in range(0, 12):
        for j in range(0, 6):
            index = i * 6 + j
            # print(i  j  index)
            df_temp = df[df['hour'] == i]
            counts = df_temp[df_temp['min'] == j]['lonlat'].value_counts()
            center = getCenter(counts)
            wfile.write('%d,%s\n' % (index, center))
            # print('%d %s' %(index center))
            # for k in range(0 len(counts)):
            #    print('%d %s %d'%(index counts.index[k] counts[k]))
            # wfile.write(counts.index[k] + ' ' + str(counts[k]) + '\ ')
    wfile.close()
# 结束时间
elapsed = (time.clock() - start)
print("Test Time used:", int(elapsed / 60), "min")