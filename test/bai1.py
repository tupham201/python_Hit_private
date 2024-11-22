n =1000
print("Nhập số x cần tính e mũ x là: ")
x =int(input())
ans = 1 
tg = 1
for i in range(1,n):
    tg =tg*x/i
    ans += tg
print(f'e^{x} = {ans}')