import pandas as pd
ser= pd.Series([3456,890,450,67892,34677,78902,56711\
,68291,637632,25723,236,1189,345,256517])

print('Top 3 smallest area are:-')
print(ser.sort_values(ascending=False).tail(3))
print('Top 3 biggest area are:-')
print(ser.sort_values(ascending=False).head(3))
