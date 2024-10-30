def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

messages = {
            'welcome': 'Welcome to Calculator!',
            'first_num': 'What\'s the first number?',
            'invalid_num': 'Hmm... that doesn\'t look like a valid number.',
            'second_num': 'What\'s the second number?',
            'operation_prompt': 'What operation would you like to perform?\n'
                                '1) Add 2) Subtract 3) Multiply 4) Divide',
            'valid_operations': 'You must choose 1, 2, 3, or 4',
            'reuse_calc': 'Would you like to use Calculator again? y/n',
}

prompt('Welcome to Calculator!')

re_prompt = True

while re_prompt:
    prompt("What's the first number?")
    number1 = input()

    while invalid_number(number1):
        prompt("Hmm... that doesn't look like a valid number.")
        number1 = input()

    prompt("What's the second number?")
    number2 = input()

    while invalid_number(number2):
        prompt("Hmm... that doesn't look like a valid number.")
        number2 = input()

    prompt("What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide")
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt("You must choose 1, 2, 3, or 4")
        operation = input()

    match operation:
        case "1":
            output = int(number1) + int(number2)
        case "2":
            output = int(number1) - int(number2)
        case "3":
            output = int(number1) * int(number2)
        case "4":
            output = int(number1) / int(number2)

    prompt(f"The result is {output}")

    prompt('Would you like to use the calculator again? y/n\n')
    ask_for_relcalculation = input()

    match ask_for_relcalculation:
        case 'y':
            re_prompt = True
        case 'n':
            re_prompt = False
            print('Goodbye.')