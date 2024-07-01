name = 'hemen$dra'
index = name.index('$')
l1 = []
for i in name:
    l1.append(i)
l1.pop(5)
l1 = l1[::-1]
l1.insert(5,'$')
s = ''
for k in l1:
    s+=k

print(name)
print(s)