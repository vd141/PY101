'''
In the previous problem, our first answer added 'Dino" to the list like this:
'''
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append("Dino")
'''
How can we add multiple items to our list? Replace the call to append with another method invocation.

We can use the extend method, which takes an iterable as an argument and adds its elements to the collectible
'''
flintstones.extend(['Dino', 'Hoppy'])
print(flintstones)