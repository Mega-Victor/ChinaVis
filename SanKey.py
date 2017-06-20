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



for days in range(10,27):
    df = pd.read_csv('F:\ChinaVis/allData/data_labeled/201704%d_labeled.csv'%days, sep=',')
    df['recidt'] = (df.recitime / 1000).apply(time.localtime)
    df['hour'] = df['recidt'].apply(getHour)
    df['month'] = df['recidt'].apply(getMonth)
    df['day'] = df['recidt'].apply(getDay)
    df['date'] = df['month'].astype(str) + '/' + df['day'].astype(str)
    df[['date','city','dist','type']].to_excel("F:/dcdt201704%d.xlsx"%days,index=False)