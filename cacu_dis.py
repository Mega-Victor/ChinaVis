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
    for i in combinations(phone_list_500,2):
        tr1 = pd.read_csv('F:\ChinaVis/trace_phone/%d/trace-%s.txt'% (day,i[0]),sep=',')

        tr2 = pd.read_csv('F:\ChinaVis/trace_phone/%d/trace-%s.txt' %(day,i[1]), sep=',')
        d = 0
        for n in range(0, 143):
            d += getDistance(tr1.loc[n][1], tr1.loc[n][2], tr2.loc[n][1], tr2.loc[n][2])
        d=d/144
        if (0<d<5):
            print(str(i[0])+','+str(i[1])+','+str(d))
            l.append(str(i[0]) + ',' + str(i[1]) + ',' + str(d))
            l.append('\n')
    print("%d"%day+'统计结束')
    f = open('F:\ChinaVis/trace_phone_cau/%d.txt'%day ,'w')
    for m in l:
        f.write(m)
    f.close()
    print("%d"%day+'写文件结束')

# 结束时间
elapsed = (time.clock() - start)
print("Test Time used:", int(elapsed / 60), "min")