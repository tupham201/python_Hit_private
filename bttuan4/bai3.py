list1 = [1,2,2,1]
list2 = [2,2]
ans =[]
if len(list1) > len(list2):
    for i in range(len(list2)):
        for j in range(len(list1)):
            if list2[i] == list1[j]:
                ans.append(list1[j])
                break
else:
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                ans.append(list1[j])
                break
print(ans)