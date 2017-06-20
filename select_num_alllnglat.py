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
    for i in phone_list_500:
        df=data[data['phone']==i][['phone','lng','lat']]
        df.to_csv("F:\ChinaVis/trace_phoneall/%d/%s.csv"%(day,i))
    print('finish',day)
