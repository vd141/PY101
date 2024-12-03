'''
What does the last line in the following code output?
'''

dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)

'''
num_list is a reference to a list in dictionary. using the append method mutates
this list, because list is a mutable object

list: [1, 2]
dictionary: {'first': [1, 2]}
'''