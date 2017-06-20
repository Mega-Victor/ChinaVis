import math
import pandas as pd
import pygame

# 开始时间
import time
from itertools import combinations, product

start = time.clock()
def getDistance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
df1=pd.read_csv('F:\ChinaVis/trace_phone/21_phoneNum.txt',sep=',')

phone_1_list=df1['666666'].tolist()
for p in phone_1_list:
    tr1 = pd.read_csv('F:\ChinaVis/trace_phone/21/trace-%s.txt' %p, sep=',')
    l = []
    for day in range(1,64):
        df2=pd.read_csv('F:\ChinaVis/trace_phone/%d_phoneNum.txt'%day,sep=',')
        phone_2_list = df2['666666'].tolist()
        for i in phone_2_list:
            tr2 = pd.read_csv('F:\ChinaVis/trace_phone/%d/trace-%d.txt' %(day,i), sep=',')
            d = 0
            for n in range(0, 143):
                d += getDistance(tr1.loc[n][1], tr1.loc[n][2], tr2.loc[n][1], tr2.loc[n][2])
            d=d/144
            print(d)
            if (0<d<11):#第二个号码是几号，第一个号码，第二个号码，距离
                print(str(day)+','+str(p)+','+str(i)+','+str(d))
                l.append(str(day)+','+str(p) + ',' + str(i) + ',' + str(d))
                l.append('\n')
        print("%d"%day+'统计结束')
    if len(l) != 0:
        f = open('F:\ChinaVis/trace_phone_cau/%d.txt'%p ,'w')
        for m in l:
            f.write(m)
        f.close()
    print("%d"%day+'写文件结束')


# 结束时间
elapsed = (time.clock() - start)
print("Test Time used:", int(elapsed / 60), "min")
file='D:/CloudMusic/devi.mp3'
pygame.mixer.init()
print("播放音乐1")
track = pygame.mixer.music.load(file)

pygame.mixer.music.play()
time.sleep(5)
pygame.mixer.music.stop()