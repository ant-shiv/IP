import matplotlib.pyplot as plt
import numpy as np
x1 = [10,20,30]
y1 = [20,40,10]
x2 = [10,20,30]
y2 = [40,10,20]
plt.plot(x1,y1 ,"b" ,linewidth = 3,label ='line1' )
plt.plot(x2,y2 ,"r-." ,linewidth = 5,label='line2' ) 
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Comparison of 2 products')
plt.legend(loc="upper right")
plt.show()