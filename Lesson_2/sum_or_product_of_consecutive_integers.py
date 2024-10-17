# Sum or Product of Consecutive Integers

upper_limit = int(input('Please enter an integer greater than 0: '))
operation = input('Enter "s" to compute the sum, or "p" to compute the product. ')

if upper_limit <= 0:
    print('Please enter an integer greater than 0.')
    break

match operation:
    case 's':
        sum = 0
        for i in range(1, upper_limit+1):
            sum += i
        print(f'The sum of the integers between 1 and {upper_limit} is {sum}')
    case 'p':
        product = 1
        for i in range(1, upper_limit+1):
            product *= i
        print(f'The product of the integers between 1 and {upper_limit} is {product}')
    case _:
        print('Please enter a valid option: s or p')