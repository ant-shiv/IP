import pandas as pd

data = {'State': ['Mumbai', 'Delhi', 'TN','KN'],
        'Cases':[5000,4000,3000,2100]
        }
corona = pd.DataFrame(data,index=['100','110 ','120','130'])
reco = [1000,1500,1500,1000]
corona['recovery'] = reco
corona.pop('Cases')

print(corona)
#DataFrameName.insert(loc, column, value, allow_duplicates = False)