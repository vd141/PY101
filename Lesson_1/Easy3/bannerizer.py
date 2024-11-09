# bannerizer
# word wrap sentences that are too long to fit
# number of new strings created is len(original string)/length
# each new string has length of length or less


def print_in_box(string, length = float('Inf')):

    if len(string) > length:
        quantity_of_new_strings = abs(-len(string) // length) # ceiling division
        new_string_list = []
        lower = 0
        for i in range(quantity_of_new_strings):
            upper = lower + length
            new_string_list.append(string[lower:upper])
            lower = upper
    # string = string[:length] # truncate string length
    string_len = len(string)
    if len(string) > length:
        print(f'+-{'-' * length}-+')
        print(f'| {' ' * length} |')
        for substring in new_string_list:
            print(f'| {substring}{(length - len(substring)) * ' '} |')
        print(f'| {' ' * length} |')
        print(f'+-{'-' * length}-+')
    else:
        print(f'+-{'-' * string_len}-+')
        print(f'| {' ' * string_len} |')
        print(f'| {string} |')
        print(f'| {' ' * string_len} |')
        print(f'+-{'-' * string_len}-+')

print_in_box('To boldly go where no one has gone before.', 5)
print_in_box('')