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

    if operation == '+':
        print('{} + {} = '.format(x, y))
        print(calculator.add(x, y))

    elif operation == '-':
        print('{} - {} = '.format(x, y))
        print(calculator.subtract(x, y))

    elif operation == '*':
        print('{} * {} = '.format(x, y))
        print(calculator.multiply(x, y))

    elif operation == '/':
        print('{} + {} = '.format(x, y))
        print(calculator.divide(x, y))
    else:
        print('invalid operation')

    again()


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
