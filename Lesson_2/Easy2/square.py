from multiply import multiply

def square(num1):
    return multiply(num1, num1)

print(square(5) == 25)   # True
print(square(-8) == 64)  # True