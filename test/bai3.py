print("Nhập vào 1 chuỗi: ")
st = input()
i = 0
ans = ""
while i != len(st):
    if(st[i]>='0' and st[i] <='9'):
        k = int(st[i])
        tg = ""
        tg1 = i + 2
        i+=2
        for j in range(tg1,len(st)):
            i+=1
            if st[j] == ']':
                break
            tg += st[j]
        for j in range(k):
            ans +=tg
    else:
        ans += st[i]
        i += 1
print(ans)