'''
Clean up the words.

loop through string. add characters to list. if a character is a non-alphanum, 
convert to space. if previous character was non-alphanum, do not add to list

loop through string. add alpha characters to list. if character is not alpha,
add space to list if previous character isn't a space or if list is empty
'''

def clean_up(string):
    cleaned_string_list = []

    for char in string:
        if char.isalpha():
            cleaned_string_list.append(char)
        else:
            if ((len(cleaned_string_list) == 0) or 
                    (cleaned_string_list[-1] != ' ')):
                cleaned_string_list.append(' ')
    return ''.join(cleaned_string_list)

print(clean_up("---what's my +*& line?") == " what s my line ")
# True