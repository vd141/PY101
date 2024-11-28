'''
How can we add the family pet, "Dino", to the following list?
'''
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
'''
There are two ways. We can use the built-in list method, append(), or we can use list concatenation with the += operator.
The argument for append() can be any data type. But the operand of the augmented assignment operator must be a list that contains the string 'Dino'
'''

flintstones.append('Dino')

flintstones += ['Dino']

print(flintstones)
# ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles", "Dino", "Dino"]