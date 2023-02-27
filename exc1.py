w = True
a = True
while w:
    a = True
    number1 = int(input('Input 1 number: '))
    number2 = int(input('Input 2 number: '))
    divided_number = int(input('Input number you want to divide by: '))
    numbers = list(range(number1, number2+1))
    numbers_divided_by = []

    for i in numbers:
        if i % divided_number == 0:
            numbers_divided_by.append(i)

    print(f'In range {number1, number2} is {len(numbers_divided_by)} numbers divided by {divided_number}.')
    print(f'Plausability of number divided by {divided_number} in range {number1, number2} is {len(numbers_divided_by)/len(numbers)}.')

    while a:
        con = input('Would you like to continue! (y/n): ')
        if con == 'y':
            a = False
            w = True
        elif con == 'n':
            a = False
            w = False
        else:
            print('Wrong letter.')
            a = True
