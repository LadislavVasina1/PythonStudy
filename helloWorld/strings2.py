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

# SLICING BY STEPS
print(parrot[0:6:2])  # Nre - Slice stars at index position 0 - It extends up to position 6 - We step through the sequence in steps of 2
print(parrot[0:6:3])  # Nw

number = "9,223;372:036 854,775;807"
separators = number[1::4]  # From index 1 (this index including) get every fourth char
print(separators)

# PRINTING VALUES SEPARATED BY MULTIPLE SEPARATORS
values = "".join(char if char not in separators else " " for char in number).split()
print(values)
print([int(val) for val in values])





