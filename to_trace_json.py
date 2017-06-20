import time
import pandas as pd
import json

# 开始时间
start = time.clock()
path = 'F:\ChinaVis/20170223_clean.csv'
data = pd.read_csv(path, encoding='utf-8')
recitimelist = data.as_matrix(['recitime'])
conntimelist = data.as_matrix(['conntime'])
tr_recitimelistt = []
tr_conntimelist = []

for timestamp in recitimelist[:]:
    tr_timestamp = time.strftime("%Y%m%d %H:%M:%S", time.localtime(timestamp / 1000))
    tr_recitimelistt.append(tr_timestamp)

for timestamp in conntimelist[:]:
    tr_timestamp = time.strftime("%Y%m%d %H:%M:%S", time.localtime(timestamp / 1000))
    tr_conntimelist.append(tr_timestamp)

data['recitime'] = pd.DataFrame(tr_recitimelistt)
data['conntime'] = pd.DataFrame(tr_conntimelist)

# # 除去时间差在一个小时以上的数据
# halfhour_data = data[(data['recitime']-data['conntime']).astype(int) <= 3600]
# print(halfhour_data.info())

dropdup_data = data.drop_duplicates()

# # 丢掉95588
# drop_95588_data = dropdup_data[dropdup_data['phone'] != 95588]
# print(drop_95588_data.count())


print(dropdup_data.info())
data_phonenumber = dropdup_data[['md5', 'phone', 'coord','count','conntime', 'recitime']]

j = (data_phonenumber.groupby(['phone', 'md5'], as_index=False)
     .apply(lambda x: x[[ 'coord','count', 'conntime', 'recitime']].to_dict('r'))
     .reset_index()
     .rename(columns={0: 'data'})
     .to_json(orient='records'))
data = json.dumps(json.loads(j), indent=2, sort_keys=True)
with open('F:\\20170223_trace.json', 'w') as f:
    f.write(data)

# phone_dict['phoneNum'].append({'data': [d]})
#     # for d in p_data.to_dict(orient='records'):
#     #     phone_dict['phoneNum'].append({'data': [d]})

# with open('F:\\20170223_trace.json', 'w') as f:
#     f.write(data)


# 结束时间
elapsed = (time.clock() - start)
print("Test Time used:", int(elapsed / 60), "min")
