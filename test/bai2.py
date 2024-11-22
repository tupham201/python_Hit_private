print("Nhập từ: ")
st = input()
dir = {}
for _ in range(len(st)):
    key = st[_]
    dir[key] = 0
for _ in range(len(st)):
    key = st[_]
    dir[key] += 1
print(dir)
