print("nhập số n: ")
n = int(input())
a = [input()for _ in range(n)]
print("nhập số m: ")
m = int(input())
b = [input()for _ in range(m)]
c = []
index = 0
for i in range(min(n,m)):
    c.append(a[index])
    c.append(b[index])
    index += 1
while index < n:
    c.append(a[index])
    index += 1
while index < m:
    c.append(b[index])
    index += 1
print(c)