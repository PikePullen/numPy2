import numpy as np

"""These all give the same result in the end. Initially we do it with just basic Python.
We will do the numpy specific methods at the bottom"""

a = np.array([1,2])
b = np.array([3,4])

print("PY***********************")
dot = 0
for e, f in zip(a,b):
    dot += e * f

print(dot)

print("PY***********************")
dot = 0
for i in range(len(a)):
    dot += a[i] * b[i]

print(dot)

print("NP***********************")
dot = 0
dot = np.sum(a * b)

print(dot)

print("NP***********************")
dot = 0
dot = (a * b).sum()

print(dot)

print("NP***********************")
dot = 0
dot = np.dot(a, b)

print(dot)

print("NP***********************")
dot = 0
dot = a.dot(b)

print(dot)

print("NP***********************")
dot = 0
dot = a @ b

print(dot)