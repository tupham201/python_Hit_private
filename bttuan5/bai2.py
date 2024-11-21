dky = set(input().split())
da_dky = set(input().split())

chua_dky = dky - da_dky
print(chua_dky)

total = dky | da_dky
k = list(total)
print(k)

print(sorted(k))