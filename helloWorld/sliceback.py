letters = "abcdefghijklmnopqrstuvwxyz"
length = len(letters)

reverse = letters[25:0:-1]  # Starts at index 25, which is the z, and I set the stop value to 0 (omitted) and use the step of -1.
forwards = letters[:26:1]   # Starts at the beginning, which is the a, and I set the stop value to 26 (omitted) and use the step of 1.
print(reverse)
print(forwards)

qpo = letters[16:13:-1]
print(qpo)

edcba = letters[4::-1]
print(edcba)

lastEightReverse = letters[:length-9:-1]
print(lastEightReverse)


#************************************************************************************#
#                            ### PYTHON IDIOMS ###                                   #
#************************************************************************************#
backwards = letters[::-1]  # Python reverse idiom. Use this to reverse string.
print(backwards)

lastXChars = letters[-4:]  # Printing last X characters
print(lastXChars)

getFirstChar = letters[:1] # Printing first character. You can use letters[0] but if it would be empty code will crash
print(getFirstChar)
