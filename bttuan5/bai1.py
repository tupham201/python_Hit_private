n = int(input())
m = int(input())

a = tuple(int(input()) for i in range(n))
b = tuple(input() for i in range(m))

tbc = sum(a) / n
cnt = 0
for i in a:
    if i >= tbc:
        cnt += 1
print(f"Số lượng phần tử lớn hơn trung bình cộng là {cnt}")

evenA = tuple(_ for _ in a if _ % 2 == 0)
oddA = tuple(_ for _ in a if _ % 2 == 1)

k = input()
dem = b.count(k)
print(f"số làn xuất hiện của k là {dem}")

bb = tuple(_ for _ in b if len(_) > 5)
if len(bb)!=0:
    print(bb)
minn = min(len(a), len(b))
C = tuple((a[i], b[i]) for i in range(minn))
print(C)