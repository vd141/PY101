'''
Starting with the string famous_words, show two different ways to create a new string with
"Four score and " prepended to the front of the string

we can initialize the new string to a new variable called new_string
We can perform string concatenation by referencing the value of famous_words and concatenating it to
"Four score and " with the + operator
'''

famous_words = "seven years ago..."
new_string = "Four score and " + famous_words

'''
We can also initialize a string variable called prefix and perform an augmented assignment of famous_words to it
'''

prefixed = "Four score and "
prefixed += famous_words

print(new_string)
print(prefixed)