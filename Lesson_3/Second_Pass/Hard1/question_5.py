'''
What do you expect to happen when the greeting variable is referenced in the last
line of the code below?
'''
if False:
    greeting = "hello world"

print(greeting)
'''
Because the if statement is false, the if block never executes. so greeting is 
uninitialized. the print function will raise a NameError exception because the 
greeting variable is never initialized
'''