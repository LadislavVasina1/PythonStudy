parrot = "Norwegian Blue"

print(parrot)
# INDEXING
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()
# NEGATIVE INDEXING
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

# SLICING
print(parrot[0:6])  # print chars from 0 to 6 (6 omitted)
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])

print(parrot[10:14])
print(parrot[10:])

a = parrot[:6]
b = parrot[6:]
print(a + b)

print(parrot[:])

# NEGATIVE SLICING
print(parrot[-4:-2])
print(parrot[-4:12])


