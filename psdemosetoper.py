a = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5']
b = ['192.168.1.1', '192.168.1.3', '192.168.1.5', '192.168.1.7', '192.168.1.9']
c = [5, 6, 7, 8, 9]

# temp = [1, 3, 5]x`
x = set(a)
y = set(b)
z = set(c)
print(sorted(x.intersection(y)))
print(list(x.intersection(y)))
print()
print(x.union(y))
print()
print(x.difference(y))
print()
print(y.difference(x))