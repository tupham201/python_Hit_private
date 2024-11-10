a = [1,3,2,4,5]
for i in range(0,len(a)):
    print(a[i])
b = [i*2 for i in range(1,101)]
print(b)
n = int(input())
c = [int(input()) for _ in range(1, n + 1)]
sumc = sum(c)
print("c =", c)
print("Tổng các phần tử trong c: ", sumc)
n = int(input())
m = int(input())
d = [[int(input())for _ in range(1,n+1)]for i in range(m)]
print(d)