'''
write a one-liner to count the number of lower-case t characters in each of the
following strings:
'''
statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."
'''
we use the count string method, which takes a substring and returns the number
of time that substring appears in the parent string
'''
print(statement1.count('t'))
print(statement2.count('t'))