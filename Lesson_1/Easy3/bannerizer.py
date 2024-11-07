# bannerizer

def print_in_box(string, length = float('Inf')):

    if len(string) > length:
        string = string[:length]
    string_len = len(string)
    print(f'+-{'-' * string_len}-+')
    print(f'| {' ' * string_len} |')
    print(f'| {string} |')
    print(f'| {' ' * string_len} |')
    print(f'+-{'-' * string_len}-+')

print_in_box('To boldly go where no one has gone before.', 5)
print_in_box('')