# Strings strings

def stringy(length):
    binary = []
    for i in range(length):
        digit = '1' if i % 2 == 0 else '0'
        binary.append(digit)
    return ''.join(binary)

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True