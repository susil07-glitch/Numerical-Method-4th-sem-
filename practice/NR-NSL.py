
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2-4*x-10
def df(f,x,h=1e-10):
    return (f(x+h)-f(x-h)/(2*h))
# initial guess 
a=4

# check if at the initail guess the derivative is 0 or not 
if df(f,a)==0:
    print(f"Derivative at {a} is 0 , Choose another initial guess")
    exit(0)

#Enter tolerance error as E 
E=1e-10 

#Enter maximum number of iteration as N
N=100

#Initialize counter as itr
itr=1

#List create 
A=[]


while(itr<=N):
    c=a-f(a)/df(f,a)
    A.append(a)
    error=np.abs((c-a)/c)

    if df(f,c)==0:
        print(f"Derivative at {c} is 0 ,Choose another initial guess ")
        exit(0)
    if(error<E):
        break
    a=c
    itr+=1

if itr>N:
    print(f"Solution in not reached in {N} iterations ")
    exit(0)
else:
    print(f"solution in {itr} iteration is {c}")

    # for garaph only 

    x=np.linspace(a-2,a+5,1000)
    y=np.zeros_like(A)
    A=np.array(A)

    plt.plot(x,f(x),label='f(x)',color='red')
    plt.grid(True)
    plt.title(f"Newton-Raphson Method ")
    plt.scatter(A,y,marker='x')
    plt.axhline(0)
    plt.axvline(0)
    plt.xlabel=('x-axis')
    plt.ylabel=('y-axis')
    plt.scatter(A,f(A))

    for i in range (len(A)):
        plt.text (A[i],0,f'{itr}')
    plt.legend()
    plt.show()



