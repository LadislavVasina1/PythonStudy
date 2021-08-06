import math
for i in range(1, 13):
    print("Number {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
    print("Number {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))  # ^CENTERING

print()

print("Pi is approximately {0:12}".format(math.pi))
print("Pi is approximately {0:12f}".format(math.pi))
print("Pi is approximately {0:12.50f}".format(math.pi))
print("Pi is approximately {0:52.50f}".format(math.pi))
print("Pi is approximately {0:62.50f}".format(math.pi))
print("Pi is approximately {0:72.50f}".format(math.pi))
print("Pi is approximately {0:72.54f}".format(math.pi))


# F STRINGS - Python 3.6 or newer
print(f"Pi is approximately {math.pi:12.50f}")





