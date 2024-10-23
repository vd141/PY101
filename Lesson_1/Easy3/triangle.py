# right triangles

def triangle(width):
    for i in range(1, width + 1):
        print(f'{' ' * (width - i)}{'*' * i}')

triangle(5)
triangle(9)