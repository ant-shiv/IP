import pandas as pd
import numpy as np
data1 = {' ':[201,457,365,221,122,210],
        'Name':['R.K.Nath','Mahavir Singh','M.Asthana','V.S.Nag','S.P.Sinha','J.P.Pandey'],
        'Dept':['ENT','SKIN','MEDICINE','ENT','NEURO','CARDIOLOGY'],
        'GENDER':['M','M','F','F','M','M'],
        'Experience':[12,'null',9,5,20,1],
        'ConstFees':[300,500,250,200,500,400]}

doc = pd.DataFrame(data1, index =[201,457,365,221,122,210])                                 #create DataFrame
a = doc.iloc[::2]                                         #every second number

address = ['HR', 'UP', 'DL','DL','HR','UP']
doc['ADDRESS'] = address                                  #add column in DataFrame

doc.loc[len(doc.index)] = [111,'Jaya','CARDIO','F',6,350,'UK'] #add row in DataFrame

doc.drop(['GENDER'],axis=1, inplace=True)                 #remove data temporarily

doc.tail()                                                #last 5 values

doc['Experience'] = doc['Experience'].replace(['null'],15)     #replace values

options = ['ENT', 'SKIN']
  
# selecting rows based on condition
rslt_df = doc.loc[doc['Dept'].isin(options)]
print(rslt_df)
