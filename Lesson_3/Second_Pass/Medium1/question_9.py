'''
What will the function invocation return?
'''

def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")

bar(foo())

# returns False because foo() returns False