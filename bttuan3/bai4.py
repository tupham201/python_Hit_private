st = input()
vt = int((len(st)-1)/2)-1
kt = 0 
if(st[vt] == '@'):
    for i in range(vt,len(st)):
        if st[i] == '.':
            kt = 1
            break
if kt == 1:
    print("valid")
else:
    print("Invalid")