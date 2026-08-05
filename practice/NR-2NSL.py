
# Solution of Two non- linear equation using Newton-Raphson Method 

import numpy as np

# Define the functions
def F(x,y):
    return np.array([
        x[0]**2 + y[1]**2 - 4,   # f(x, y)
        x[0] - y[1]              # g(x, y)
    ])

# Define the Jacobian matrix
def J(x,y):
    return np.array([
        [2*x[0], 2*y[1]],   # df/dx, df/dy
        [1, -1]             # dg/dx, dg/dy
    ])

# Initial guess
x = np.array([1.0, 1.0])
y = np.array([1.0, 1.0])

# Maximum iterations
max_iter = 20

# Tolerance
tol = 1e-6

print("Iteration\t x\t\t y")

for i in range(max_iter):
    c = np.linalg.solve(J(x,y), -F(x,y))
    x = x + c
    y=y + c 

    print(f"{i+1}\t\t {x[0]:.6f}\t {y[0]:.6f}")

    if np.linalg.norm(c) < tol:
        break

print("\nApproximate Solution:")
print("x =", x[0])
print("y =", y[0])



