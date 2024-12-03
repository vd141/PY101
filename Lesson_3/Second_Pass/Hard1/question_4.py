'''
Ben was tasked to write a simple Python function to determine whether an input
string is an IP address using 4 dot-separated numbers, e.g. 10.4.5.11

Alyssa supplied Ben with a function is_an_ip_number. She asked Ben to use it. Here is
the code that Ben wrote:
'''
def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            break

    return True
'''
There are some issues with Ben's function: 
- not returning a False condition,
- not handling the case when the input string has more or less than 4 components
e.g 4.5.5 or 1.2.3.4.5: both values should be invalid
'''

'''
we would like the function to return False when the word is not an ip number
or when the input string has less than or more than 4 components. we would like it
to return True if otherwise. 

to return false if the input string has less than or more than 4 components, the
code should check if the length of dot_separated_words (a list) is != 4. if it
isn't, the function should return True

if the word is not an ip number, there should be a return True statement instead
of a break. This exits the function when any of the words are not ip numbers

new function below:
'''
def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False