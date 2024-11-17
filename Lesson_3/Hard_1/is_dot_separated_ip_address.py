'''
Code improvements Question 4


add check after splitting to see if the length of split words is 4. if not, 
invalidate input. 

return False if word is not an ip address

return True outside loop if the words are legit ip numbers
'''

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True