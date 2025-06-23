from math import ceil

def ceil_sqare(x):
    return ceil (x*x)
x = float(input("число:"))
result = ceil_sqare(x)
print(result)