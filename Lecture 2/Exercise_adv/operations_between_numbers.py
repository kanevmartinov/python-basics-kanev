N1 = int(input())
N2 = int(input())
operator = input()
operation = 0
type = ''

if operator == '+':
    operation = N1 + N2
    if operation % 2 == 0:
        type = 'even'
    else:
        type = 'odd'
    print(f'{N1} {operator} {N2} = {operation} - {type}')
elif operator == '-':
    operation = N1 - N2
    if operation % 2 == 0:
        type = 'even'
    else:
        type = 'odd'
    print(f'{N1} {operator} {N2} = {operation} - {type}')
elif operator == '*':
    operation = N1 * N2
    if operation % 2 == 0:
        type = 'even'
    else:
        type = 'odd'
    print(f'{N1} {operator} {N2} = {operation} - {type}')
elif operator == '/':
    if N2 > 0:
        operation = N1 / N2
        print(f'{N1} {operator} {N2} = {operation:.2f}')
    else:
        print(f'Cannot divide {N1} by zero')
elif operator == '%':
    if N2 > 0:
        operation = N1 % N2
        print(f'{N1} {operator} {N2} = {operation}')
    else:
        print(f'Cannot divide {N1} by zero')
