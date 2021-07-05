import pandas as pd
data={'State':['U.P','M.P','Bihar','Haryana','Punjab'],
'Toys':[4567,5678,6789,1234,5789],
'Books':[34445,45550,45840,56575,56575],
'Uniform':[100,500,500,488,400],
'Shoes':[400,600,650,700,450]}
df=pd.DataFrame(data,columns=['State','Toys','Books','Uniform','Shoes'])
print(df)
print('A. data of Toys Column')
print(df['Toys'])
print('B. data of First 3 rows Toys and Book columns (using loc)')
print(df.loc[0:3,['Toys','Books']])
print('C. data of First 2 rows State,Toys and Books columns (using iloc)')
print(df.iloc[0:2,0:3])

