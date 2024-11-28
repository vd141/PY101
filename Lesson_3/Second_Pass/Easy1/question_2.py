'''
How can you determine whether a given string ends with an exclamation mark(!)? Write some code that prints True or False
depending on whether the string ends with an exclamation mark.
'''
str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False
'''
we can use string indexing to get the last character of the string. the index of the last character of any string is -1

The syntax would look like this:
str1[-1] # !
str2[-1] # ?

We can write code that tests if the value of str1[-1] is the same value as !
'''

print(str1[-1] == '!')
print(str2[-1] == '!')