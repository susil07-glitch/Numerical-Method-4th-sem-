

import numpy as np
import matplotlib.pyplot as plt

def f(x):

    return x**2-4*x-10
#Enter the initial guess 

a=4
b=5
fa=f(a)
fb=f(b)
if fa==fb:
    print(f"Division by zero ,Choose other guess ")
    exit(0)
#Enter tolerance error as E
E=1e-10

#Enter the number of iteration as N
N=200

#Initializing the list to store the estimation at each iteration 
A=[]

#initialize the counter as
itr =1
while(itr<=N):
    c=(a*fb-b*fa)/(fb-fa)
    if(c==0):
        print(f"Process terminated due to division by Zero ")
        exit(0)

    error=np.abs((c-b)/c)
    A.append(c)
    if(error<E):
        break
    a=b
    b=c
    if(f(a)==f(b)):
        print(f"Division by Zero ,Choose other guess")
        exit(0)
    itr +=1

if(itr>N):
    print(f"Solution is not reached in {N } iterations")
else:
     print(f"Solution in {itr} iteration is {c}")

# for graph only 

x=np.linspace(a-2,b+5,1000)
y=np.zeros_like(A)
A=np.array(A)
plt.plot(x,f(x),label='f(x)',color='red')
plt.grid(True)
plt.legend()
plt.title(F"Secant Method ")
plt.axhline(0,color='black')
plt.axvline(0,color='black')
plt.scatter(A,f(A))
for j,k in enumerate(A):
    plt.text(k,0,str(j+1))
plt.scatter(A,y,marker='X',color='green')
plt.show()


