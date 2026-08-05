# Jacobi's method to solve a system of linear equations

import numpy as np 
# Define the coefficient matrix A and the constant vector B

A=np.array([
    [3,20,-1],
    [20,1,-2],
    [2,-3,20]
],dtype=float)


#Define the constant vector B 

B=np.array([
    [-18,17,25]
],dtype=float)

#Define the i initial guess for the solution vector X 
x=np.zeros(len(B))

# Tolerande error for convergence 

E=1e-10

# total number of iteration 

N=100

print("Iteration \t solution")

for k in range(N):
    x_new=np.zeros_like(x)
    for i in range(len(B)):
        s=0
        for j in range (len(B)):
            if i!=j:
                s+=A[i][j]*x[j]
        x_new[i]=(B[i]-s)/A[i][i]

    print(f"{k+1} \t\t{x_new}")
    if np.linalg.norm(x_new-x,ord=np.inf)<E:
        break
    x=x_new.copy()
print("\nApproximate Solution:")
print("x=",x[0])
print("y=",x[1])
print("z=",x[2])
    








