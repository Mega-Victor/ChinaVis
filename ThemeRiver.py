import pandas as pd
# import jieba
import os
import time
import itertools


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


for days in range(7,38):
    df = pd.read_csv('F:\ChinaVis/allData/data_labeled/%d.csv'%days, sep=',')
    df['recidt'] = (df.recitime / 1000).apply(time.localtime)
    df['hour'] = df['recidt'].apply(getHour)
    df['month'] = df['recidt'].apply(getMonth)
    df['day'] = df['recidt'].apply(getDay)
    l_type=["地产广告","冒充身份","色情服务","违禁推销","办证发票"]
    # type=["地产广告","打折促销","冒充身份","色情服务","违禁推销","非法博彩","办证发票","教育移民","招聘广告","其他类型"]
    hour=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
    l=[]
    for i in l_type:
        for hours in range(0,24):
            data = df[df['hour'] == hours]['type']
            type_list = data.tolist()
            # len_list = len(type_list)
            b=type_list.count(i)
            l.append(str('['+repr(str(hours))+','+str(b)+','+repr(str(i))+']'+'\n'))
    for hour in range(0,24):
        data = df[df['hour'] == hour]['type']
        type_list = data.tolist()
        c = (type_list.count("打折促销") + type_list.count("非法博彩") + type_list.count("教育移民")
        +type_list.count("招聘广告") + type_list.count("其他类型"))
        l.append(str('['+repr(str(hour))+','+str(c)+','+repr('其他类型')+']'+'\n'))

    f=open('F:\ChinaVis/ThemeRiver_data/201702%d_ThemeRiver.xls'%days,'w')
    for i in l:
        f.write(i)
    f.close()
















    # for hours in range(0,24):
    #     data=df[df['hour'] == hours]['type']
    #     type_list=data.tolist()
    #     len_list=len(type_list)
    #     sum=0
    #     for i in type:
    #         b=type_list.count(i)
    #         sum=sum+b
    #         l.append(str('['+repr(str(hours))+','+str(b)+','+repr(str(i))+']'+','))
    #     l.append(str('['+repr(str(hours))+','+str(len_list-sum)+','+repr('其他类型')+']'+','))
    #
    # f=open('F:\ChinaVis/ThemeRiver_data/201702%d_ThemeRiver.txt'%days,'w')
    # for i in l:
    #     f.write(i)
    # f.close()
