a = {}
print("Nhập số lượng phần tử trong dictionary: ")
n = int(input())
for _ in range(n):
    key = input()
    value = input()
    a[key] = value
dir2={}
for i in a.keys():
    if a[i] in dir2.keys():
        dir2[a[i]]="None"
    else:
        dir2[a[i]]=i
print(dir2)