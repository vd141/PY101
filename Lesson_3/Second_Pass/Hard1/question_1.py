'''
Will the following functinos return the same results?
'''

def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

# the first function will return the dictionary because the opening brace of the 
# dictionary immediately follows the return keyword

# the second function returns None because nothing immediately follows the return
# keyword. The dict is on the next line, which is not read as Python's return 
# expression