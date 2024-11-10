print("Nhập vào số k: ")
k = int(input())
lt = [int(input())for _ in range(k)]
print("Nhập n: ")
n = int(input())
print("Nhập m: ")
m = int(input())
if m*n > k:
    print("không thể xây dựng ma trận ")
else:
    index = 0
    ans = []
    for i in range(n):
        mt = []
        for j in range(m):
            mt.append(lt[index])
            index +=1
        ans.append(mt)
    print(ans)
