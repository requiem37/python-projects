try:
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    op = input('Выберите операцию (+ - * /): ')

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':

        if num2 != 0:
            result = num1 / num2
        else:
            print('Ошибка! Деление на ноль!')
    else:
        print('Ошибка! Неверная операция!')

except VallueError:
    print('Ошибка! Введены не цифры!')

print('result: ', result)
