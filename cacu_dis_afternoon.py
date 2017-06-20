import math
import pandas as pd
import numpy as np

# 开始时间
import time

start = time.clock()
def getDistance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
l=[]
df_phone = pd.read_csv("F:/ChinaVis/phoneNum.txt",sep='\n')
df_phone_list = df_phone.values
for phoneNum in df_phone_list:
    tr1 = pd.read_csv('F:\ChinaVis/trace_phone/0417_2/trace-%d.txt'% phoneNum[0],sep=',')
    for phone in df_phone_list:
        if phoneNum != phone:
            tr2 = pd.read_csv('F:\ChinaVis/trace_phone/0417_2/trace-%d.txt' % phone[0], sep=',')
            d = 0
            for i in range(0, 71):
                d += getDistance(tr1.loc[i][1], tr1.loc[i][2], tr2.loc[i][1], tr2.loc[i][2])
            d=d/71
            print(str(phoneNum[0])+','+str(phone[0])+','+str(d))
            l.append(str(phoneNum[0])+','+str(phone[0])+','+str(d))
            l.append('\n')
f=open('F:/result_2.txt','w')
for i in l:
    f.write(i)
f.close()

# 结束时间
elapsed = (time.clock() - start)
print("Test Time used:", int(elapsed / 60), "min")