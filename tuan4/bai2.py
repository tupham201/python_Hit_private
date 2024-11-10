n = int(input())
a = [int(input())for i in range(1,n+1)]
a.sort()
print(a)
print(f'Gía trị min là: {a[0]}')
print(f'Gía trị max là: {a[n-1]}')
for i in range(1,n+1):
    if a[i] % 2 == 0:
        print(a[i])
        break
k = int(input())
a.insert(4,k)
print(a)
for i in range(0,n-1):
    if a[i] % 2 == 0:
        a.remove(a[i])
print(a)
m = int(input())
b = [int(input())for _ in range(1,m+1)]
b = b*2
b.reverse()
c = a + b
print(c)