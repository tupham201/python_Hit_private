import math
n = int(input())
x = math.sqrt(n)
if x*x == n:
    print(int(x-2))
else:
    print(int(x-1))
