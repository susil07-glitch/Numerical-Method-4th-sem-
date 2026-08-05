
import numpy as np 
import scipy.integrate as integrate
import matplotlib.pyplot as plt 
import sympy as sp



fun=input("Enter the iteration function  of x using space\t")

def f(x):
    try:
        return eval(fun)
    except:
        print("invalid syntax ")
        exit(0)
a=float(input("Entert lower limit \t"))
b=float(input("Enter upper limit \t"))
n=int(input ("Enter no.of interval\t"))
if(n%2!=0):
    print(f" No. of interval must be even")
    exit(0)
h=(b-a)/n
x=np.linspace(a,b,n+1)
y=[f(x) for x in x]
i=0
i+=y[0]+y[-1]
i+=4*np.sum(y[1:-1:2])
i+=2*np.sum(y[2:-1:2])
i*=h/3

print(f"Approximate integral by simpson 1/3 rule :{i}")

exact_int=integrate.quad(lambda x:f(x),a,b)[0]
print(f"Exact integral:{exact_int}")
error=abs(i-exact_int)
print(f'Error:{error:.2e}')
w=sp.symbols('w')
x1=np.linspace(a-5,b+5,1000)
plt.plot(x1,f(x1),label='Intergrant function',color='red',linewidth=2)
for i in range (0,n-1,2):
    x=x[i:i+3]
    y=f(x)
    lp=0
    for j in range (len(x)):
        bp=1
        for k in range (len(x)):
            if k!=j:
                bp*=(w-x[k])/(x[j]-x[k])
        lp+=bp*y[j] 
    lag_poly=sp.nsimplify(lp.evalf(),rational=True,tolerance=1e-10)  
    lag_poly1=sp.simplify(lag_poly)
    lag_p=sp.lambdify(w,lag_poly1,'numpy')
    x1=np.linspace(x[0],x[2],1000)

    plt.plot(x1,lag_poly(x1),color='blue',linewidth=2)
    plt.fill_between(x1,f(x1),lag_p(x1),color='yellow')
    plt.fill_between(x1,0,lag_p(x1),hatch='..' ,facecolor='none')
    for l in range (0,3,2):
        x2=X[l]
        l_p=lag_p(x2)
        plt.plot((x2,x2),(0,l_p),color='green')



plt.show()








