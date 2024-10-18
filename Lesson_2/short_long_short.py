# Short Long Short

# Write a functino that takes two strings as arguments, determines the length of
# the two strings, and then returns the result of concatenating the shorter
# string, the longer string, and the shorter string once again. You may assume
# that the strings are of different lengths.

def short_long_short(str1, str2):
    if len(str1) <= len(str2):
        return str2.join([str1, str1,])
    else:
        return str1.join([str2, str2, ])

str1 = input('Give me a string. ')
str2 = input('Give me another string. ')

print(short_long_short(str1, str2))