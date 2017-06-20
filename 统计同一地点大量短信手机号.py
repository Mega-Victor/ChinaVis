import pandas as pd
import time

start = time.clock()
for day in range(1,63):
    df=pd.read_csv('F:/ChinaVis/allData/data_labeled/%d.csv'%day,sep=',')
    lng_list=df['lng'].tolist()
    lat_list=df['lat'].tolist()
    phone_list=df['phone'].tolist()
    phone_list_dep=list(set(phone_list))
    lat_list_dep=list(set(lat_list))
    lng_list_dep=list(set(lng_list))
    l=[]
    for phone in phone_list_dep:
        df1 = df[df['phone']==phone]
        if len(df1)>200:
            for lng in lng_list_dep:
                df2=df1[df1['lng']==lng]
                if len(df2)>200:
                    for lat in lat_list_dep:
                        df3=df2[df2['lat']==lat]
                        if len(df3)>200:
                            b=str(str(phone) + ',' + str(lng) + ',' + str(lat) + ',' + str(len(df3)))
                            print(day,b)
                            l.append(b)
    print('count finish*************************************************')
    f=open("F:/count_%d.xls"%day,'w')
    for i in l:
        print(i)
        f.write(i+'\n')
    f.close()
    print('finish writing')
# 结束时间
elapsed = (time.clock() - start)
print("Test Time used:", int(elapsed / 60), "min")
# for phone in phone_list_dep:
#     df_data=df[df['phone']==phone]
#     count=len(df_data)
#     print(phone,',',count,',',df_data['lng'].var()+df_data['lat'].var())

