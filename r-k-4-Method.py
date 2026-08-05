
#solution of ODE by R-k-4 Method #

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

slope=input('Enter dy/dx interval of x and y using space')

def f(x,y):
    return eval(slope)
x=float(input('Enter inital valur of x'))
y=float (input("Enter initial value of y"))
h= float(input('Ente the stpe-size'))

n=int(input('Ente the no. of steps'))
xval=[]
yval=[]
table=[]
for i in range (n):
    k1=h*f(x,y)
    k2=h*f(x+h/2,y+k1/2)
    k3=h*f(x+h/2,y+k2/2)
    k4=h*f(x+h/2,y+k3)
    y=y+(1/6)*(k1+2*k2+2*k3+k4)
    x+=h
    xval.append(x)
    yval.append(y)
    table.append([x,y])
T=pd.DataFrame(table,columns=['x','y'])
print('Approximate solution by R-k-4 method:')
print(T.to_string)
plt.plot(xval,yval,label='solution by R-K-4 Method',marker='x')

plt.show()