n = int(input())    
i = 1
while(n!=0):
    st = input()
    a = int(input())
    b = int(input())
    s = a + b
    if s < 100:
        print(i,st,"Yếu")
    if s>=100 and s < 150:
        print(i,st,"Khá")
    if s>=150 and s < 190:
        print(i,st,"Giỏi")
    if s>=190:
        print(i,st,"Xuất sắc")
    i +=1
    n -=1