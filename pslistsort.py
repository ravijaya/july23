duplicates = [2.2, 0.98, 1.2, 0.67, 2.2, 0.98, 1.2, 0.67, 2.2, 0.98, 1.2, 0.67]

duplicates.sort()  # inplace edit
print(duplicates)
print()

duplicates.sort(reverse=True)  # keyword arguments
print(duplicates)
print()

duplicates = [2.2, 0.98, 1.2, 0.67, 2.2, 0.98, 1.2, 0.67, 2.2, 0.98, 1.2, 0.67]
duplicates.reverse()  # inplace edit
print(duplicates)
print()

duplicates = [2.2, 0.98, 1.2, 0.67, 2.2, 0.98, 1.2, 0.67, 2.2, 0.98, 1.2, 0.67]
s = sorted(duplicates, reverse=True)
print(s)
print(duplicates)
