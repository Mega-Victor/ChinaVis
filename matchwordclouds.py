import json
from pandas.io.json import json_normalize
f=open('F:/20170223_trace.json',encoding='utf-8')
data = json.load(f)
result = json_normalize(data,'phone', ['coord', 'count',['conntime', 'recitime']])
print(result)