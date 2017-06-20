import math
import pandas as pd

# 开始时间
import time
from itertools import combinations

start = time.clock()
def getDistance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
for day in range(1,64):
    data=pd.read_csv('F:/ChinaVis/allData/data_labeled/%d.csv'%day,sep=',')
    phone_list=data['phone'].tolist()
    phone_list=list(set(phone_list))
    phone_list_500=[]
    for phone in phone_list:
        phonedata=data[data['phone']==phone]
        if len(phonedata)>500:
            phone_list_500.append(phone)
    l=[]
    for i in phone_list_500:
        tr1 = pd.read_csv('F:\ChinaVis/trace_phoneall/%d/%s.csv'% (day,i),sep=',')

        lng_var=tr1['lng'].values.std()
        lat_var=tr1['lat'].values.std()
        if lng_var<0.03:
            if lat_var<0.03:
                b=str(str(i) + ',' + str(lng_var) + ',' + str(lat_var))
                l.append(b)
                l.append('\n')
    f = open('F:\ChinaVis/trace_phoneall_cau/%d.txt'%day ,'w')
    for m in l:
        f.write(m)
    f.close()
    print("%d"%day+'写文件结束')

# 结束时间
elapsed = (time.clock() - start)
print("Test Time used:", int(elapsed / 60), "min")