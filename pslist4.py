tiny = [2.2, 0.98, 1.2, 0.67]

print(tiny + tiny)
print()
print(tiny * 3)
print()

duplicates = [2.2, 0.98, 1.2, 0.67, 2.2, 0.98, 1.2, 0.67, 2.2, 0.98, 1.2, 0.67]
print(set(duplicates))  # unordered collection
uniq = list(set(duplicates))
print(uniq)

