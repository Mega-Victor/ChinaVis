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



l=[]
l_type = ["地产广告", "冒充身份", "色情服务", "违禁推销", "办证发票"]

for days in range(38, 64):
    df = pd.read_csv('F:\ChinaVis/allData/data_labeled/%d.csv' % days, sep=',')
    data_dichan = df[df['type'] =="地产广告" ]
    data_maochong = df[df['type'] =="冒充身份" ]
    data_seqing = df[df['type'] =="色情服务" ]
    data_weijin = df[df['type'] =="违禁推销" ]
    data_banzheng = df[df['type'] =="办证发票" ]
    data_dazhe=df[df['type'] == "打折促销"]
    data_bocai=df[df['type'] == "非法博彩"]
    data_jiaoyu=df[df['type'] == "教育移民"]
    data_zhanpin=df[df['type'] == "招聘广告"]
    data_qita=df[df['type'] == "其他类型"]
    count=(str(len(data_banzheng)))#####################################
    print(days,count)
    count_other=(len(df)-len(data_dazhe)+len(data_bocai)+len(data_jiaoyu)+len(data_zhanpin)+len(data_qita))
    # l.append(str('['+repr(str(hour))+','+str(c)+','+repr('其他类型')+']'+'\n'))
    l.append(str('['+repr(str(days-38))+','+str(count_other)+','+repr(str("其他类型"))+']'+','))###########################

f=open('F:\ChinaVis/ThemeRiver_data/river.txt','w')
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
