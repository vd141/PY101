# bannerizer

def print_in_box(string):
    string_len = len(string)
    print(f'+-{'-' * string_len}-+')
    print(f'| {' ' * string_len} |')
    print(f'| {string} |')
    print(f'| {' ' * string_len} |')
    print(f'+-{'-' * string_len}-+')

print_in_box('To boldly go where no one has gone before.')
print_in_box('')