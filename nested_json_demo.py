import pandas as pd
import json
from json import dumps

df = pd.DataFrame([["A", "2014/01/01", "2014/01/02", "A", -0.0061, "A"],
                   ["A", "2015/07/11", "2015/08/21", "A", 1.50, "A"],
                   ["C", "2016/01/01", "2016/01/05", "U", 2.75, "R"],
                   ["D", "2013/05/19", "2014/09/30", "Q", -100.0, "N"],
                   ["B", "2015/08/22", "2015/09/01", "T", 10.0, "R"]],
                   columns=["P", "Start", "End", "Category", "Value", "Group"])

json_dict = {}
json_dict['group_list'] = []

for grp, grp_data in df.groupby('Group'):
    grp_dict = {}
    grp_dict['group'] = grp

    for category, category_data in grp_data.groupby('Category'):
        grp_dict['category_list'] = []
        category_dict = {}
        category_dict['category'] = category
        category_dict['p_list'] = []
        for p, p_data in category_data.groupby('P'):
            p_data = p_data.drop(['Category', 'Group'], axis=1).set_index('P')
            for d in p_data.to_dict(orient='records'):
                category_dict['p_list'].append({'p': p, 'date_list': [d]})
        grp_dict['category_list'].append(category_dict)
    json_dict['group_list'].append(grp_dict)
json_out = dumps(json_dict)
parsed = json.loads(json_out)

data=json.dumps(parsed, indent=4, sort_keys=True)
