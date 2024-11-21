info_stu = {
    'ID': 2020601001,
    'private_info':{
        'name': "Ai do hoc Haui"
    }
}
print("=================================")
if info_stu.get('ID') == 2020601001:
    print(info_stu.get('private_info').get('name'))

#print(info_dirct)
#print(info_dirct.keys())
#print(info_dirct.values())