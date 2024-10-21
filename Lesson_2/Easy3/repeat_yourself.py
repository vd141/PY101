# write a function that takes two arguments, a string and a positive integer, 
# then prints the string as many times as the integer indicates

def repeat(a_string, an_integer):
    for _ in range(an_integer):
        print(a_string)

repeat('Hello', 3)