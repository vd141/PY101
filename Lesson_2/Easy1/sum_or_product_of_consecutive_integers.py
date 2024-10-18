# Sum or Product of Consecutive Integers

def product(lower, upper):
    product = 1
    for i in range(lower, upper+1):
        product *= i
    return product

def sum_(lower, upper):
    sum = 0
    for i in range(lower, upper+1):
        sum += i
    return sum

maximum = int(input('Please enter an integer greater than 0: '))
sum_or_product = input('Enter "s" to compute the sum, or "p" to compute '
                       'the product. ')

if sum_or_product == 's':
    print(f'The sum of the integers between 1 and {maximum} is '
          f'{sum_(1, maximum)}')
elif sum_or_product == 'p':
    print(f'The product of the integers between 1 and {maximum} '
          f'is {product(1,maximum)}')
else:
    print('Please enter either p or s ')