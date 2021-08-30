menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(meal)


for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end=" ")
    print()

# for i in range(0, len(menu)):
#     for j in range(0, len(menu[i])):
#         if "spam" not in menu[i][j]:
#             print(menu[i][j])
#     print()
