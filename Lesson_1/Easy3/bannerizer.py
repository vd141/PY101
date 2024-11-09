'''
bannerizer
word wrap sentences that are too long to fit
number of new strings created is len(original string)/length
each new string has length of length or less
'''

def wrapped_string(string, length):
    quantity_of_new_strings = abs(-len(string) // length) # ceiling division
    new_string_list = []
    lower_index = 0

    for _ in range(quantity_of_new_strings):
        upper_index = lower_index + length
        new_string_list.append(string[lower_index:upper_index])
        lower_index = upper_index

    return new_string_list

def print_header_footer(length):
    print(f'+-{'-' * length}-+')

def print_whitespace(length):
    print(f'| {' ' * length} |')

def print_in_box(string, length = float('Inf')):
    if len(string) > length:
        wrapped_string_as_list = wrapped_string(string, length)
        print_header_footer(length)
        print_whitespace(length)
        for substring in wrapped_string_as_list:
            print(f'| {substring}{(length - len(substring)) * ' '} |')
        print_whitespace(length)
        print_header_footer(length)
    else:
        print_header_footer(length)
        print_whitespace(length)
        print(f'| {string} |')
        print_whitespace(length)
        print_header_footer(length)

print_in_box('To boldly go where no one has gone before.', 5)
print_in_box('')
