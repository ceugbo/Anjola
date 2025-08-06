a = input('Enter the first number: ')
b = input('Enter the second number: ')
operator = input('Enter the arithmetic operator: ')
a = float(a)
b = float(b)
if operator == '+':
    c = a+b
    print(a, '+', b, '=', c)
elif operator == '-':
    c = a-b
    print(a, '-', b, '=', c)
elif operator == '*':
    c = a*b
    print(a, '*', b, '=', c)
elif operator == '/':
        c = a/b
        print(a, '/', b, '=', c)
else:
    print('boop!!!')
