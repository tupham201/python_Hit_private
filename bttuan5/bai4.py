import random

choice = ['CNTT', 'KHMT', 'KTPM', 'HTTT', 'DAPT']

a = {}

print("Nhập số lượng tài khoản: ")
n = int(input())

for _ in range(n):
    id = input('Nhập mã sinh viên: ')
    acc = {
        'Username': id,
        'Password': random.choice(choice) + id
    }
    a[id] = acc
print(a)