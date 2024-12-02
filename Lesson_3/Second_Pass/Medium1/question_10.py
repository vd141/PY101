'''
In Python, every object has a unique identifier that can be accessed using the id()
function. This function returns the identity of an object, which is guaranteed to be
unique for the object's lifetime. For certain basic immutable data types like short strings
or itnegers, Python might reuse the memory address for objects with the same value.
This is known as "interning".
'''

a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))

# this will print True because all integers from -5 to 256 are interned