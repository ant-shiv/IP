import pandas as pd
Area=[34567,890,450,67892,34677,78902,256711,678291,637632,25723,2367,11789,345,256517]
Ser1=pd.Series(Area)

print(Ser1.sort_values().tail(3))

print(Ser1.sort_values().head(3))