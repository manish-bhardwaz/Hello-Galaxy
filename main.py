import calculator

def calculate():
    operation = raw_input('''
    Please type in the math operation you would like to complete:
    + : Add.
    - : Subtract.
    * : Multiply.
    / : Divide.
    ''')
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : "))

    print('{} {} {} = {}'.format(x, operation, y, execute(operation, x, y)))
    again()


def execute(operation, x, y):
    switcher = {
        '+': calculator.add(x, y),
        '-': calculator.subtract(x, y),
        '*': calculator.multiply(x, y),
        '/': calculator.divide(x, y),
    }
    return switcher.get(operation, 'invalid operation')


def again():
    reiterate = raw_input('''
        Do you want to calculate again?
        Please type Y for YES or N for NO.
    ''')
    if reiterate.upper() == 'Y':
        calculate()
    elif reiterate.upper() == 'N':
        print('Bye!')
    else:
        again()


calculate()
input('strike a key to Quit')
