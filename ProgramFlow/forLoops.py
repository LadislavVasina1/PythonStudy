number = input("Please enter a series of number, using any separators you like.\n")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

# PRINTING VALUES SEPARATED BY MULTIPLE SEPARATORS
values = "".join(char if char not in separators else " " for char in number).split()
print(values)
print(sum([int(val) for val in values]))


