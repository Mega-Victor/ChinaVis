import time
import pandas as pd
import json

# 开始时间
start = time.clock()
path = 'F:\ChinaVis/20170223_datedata.csv'
data = pd.read_csv(path, encoding='utf-8')

dropdup_data = data.drop_duplicates()

print(dropdup_data.info())
data_phonenumber = dropdup_data[['coord','count','conntime_day', 'conntime_hour','recitime_day','recitime_hour']]

j = (data_phonenumber.groupby(['conntime_day', 'conntime_hour'], as_index=False)
     .apply(lambda x: x[[ 'coord','count']].to_dict('r'))
     .reset_index()
     .rename(columns={0: 'data'})
     .to_json(orient='records'))
data = json.dumps(json.loads(j), indent=2, sort_keys=True)
with open('F:\\20170223_date.json', 'w') as f:
    f.write(data)


# 结束时间
elapsed = (time.clock() - start)
print("Test Time used:", int(elapsed / 60), "min")
