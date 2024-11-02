print("Bạn muốn tính hàm: ")
st = input()
print("Tính số ")
a = int(input())
if st == "sin":
    s = 0
    t =a
    for i in range(1,10000):
        s += t
        t *= (-1)*a*a/((2*i+1)*(2*i))
    print(s)
