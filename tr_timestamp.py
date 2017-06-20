
"""
转换时间戳代码
"""
import time
import pandas as pd



path = 'F:\ChinaVis/20170223_clean_coord.csv'
data = pd.read_csv(path)
recitimelist = data.as_matrix(['recitime'])
conntimelist = data.as_matrix(['conntime'])
tr_recitimelistt = []
tr_conntimelist = []

for timestamp in recitimelist[:]:
    tr_timestamp = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime(timestamp / 1000))
    tr_recitimelistt.append(tr_timestamp)

for timestamp in conntimelist[:]:
    tr_timestamp = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime(timestamp / 1000))
    tr_conntimelist.append(tr_timestamp)

data['recitime'] = pd.DataFrame(tr_recitimelistt)
data['conntime'] = pd.DataFrame(tr_conntimelist)
data.to_csv('F:\\20170223_datedata.csv', index=False, encoding='utf_8_sig')
