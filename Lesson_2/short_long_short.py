# Short Long Short

# Write a functino that takes two strings as arguments, determines the length of
# the two strings, and then returns the result of concatenating the shorter
# string, the longer string, and teh shorter string once again. You may assume
# that the strings are of different lengths.

def short_long_short(str1, str2):
    if len(str1) <= len(str2):
        shorter = str1
        longer = str2
    else:
        longer = str1
        shorter = str2

    return longer.join([shorter, shorter,])

str1 = input('Give me a string. ')
str2 = input('Give me another string. ')

print(short_long_short(str1, str2))
