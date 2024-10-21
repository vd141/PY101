# Strings strings

def stringy(length):
    binary = []
    for i in range(length):
        if i % 2 == 0:
            binary.append('1')
        else:
            binary.append('0')
    return ''.join(binary)

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True