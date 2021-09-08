panagram = """The quick brown
 fox jumps\t over
 the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,804"
print(numbers.split(","))

seq = input()
separated = seq.split(",")
result = 0
for number in separated:
    result += int(number)
print(result)