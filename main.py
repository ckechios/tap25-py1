# This is a single line comment

# Data types
n = 5
d = 3.12
h = "total"

# inspect objects in python using dir() and help()

# Get data type
print("Data types for: n",type(n)," for d:", type(d), 'for h:', type(h))

result = d + n

# print(str(d)+"+")
# print(str(d)+"+"+n+"="+result)

# Typecasting in python
print(str(d)+"+"+str(n)+"="+str(result)[0:4])
# 012345....
# 8.1200

# To string : str()
# To Int : int()
# To Float : float()

print("String to Float",type(float("12.5454")))
print("String to int",type(int(float("12.5454"))))

# Formatted strings in Python
print(f"{d}+{n}={result}")
print(f"{d}+{n}={str(result)[0:4]}")

print("-"*20)

# define a function
def add(n1,n2):
    return n1+n2

print(f"3+6={add(3,6)}")

def divide(numerator, denominator):
    if denominator==0:
        # return -1
        return "Error"
    else:
        return numerator/denominator

print(f"8/2={divide(8,2)}")

print(f"8/0={divide(8,0)}")

