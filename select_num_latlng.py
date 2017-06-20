import pandas as pd
import numpy as np

import time
import matplotlib.pyplot as plt
for day in range(1,64):
    data=pd.read_csv('F:/ChinaVis/allData/data_labeled/%d.csv'%day,sep=',')
    phone_list=data['phone'].tolist()
    phone_list=list(set(phone_list))
    phone_list_500=[]
    for phoneNum in phone_list:
        phonedata=data[data['phone']==phoneNum]
        if len(phonedata)>500:
            phone_list_500.append(phoneNum)


    for item in phone_list_500:
        '''
        一定要修改的内容，时间戳，各个path名称
        '''
        phoneSearch = int(item)
        df = pd.read_csv('F:/ChinaVis/allData/data_labeled/%d.csv'%day,sep=',')

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


        filename = 'F:/ChinaVis/trace_phone/%d/trace-%d.txt' %(day,phoneSearch)
        wfile = open(filename, 'w')
        for i in range(0, 24):
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
