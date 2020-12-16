# Создайте приложение для перевода из одной системы счисления в другую


def convert_dec_bin(input_number):
    num_list = []
    while input_number >= 1:
        if input_number % 2 == 0:
            num_list.append(0)
        else:
            num_list.append(1)

        input_number = input_number // 2

    return ''.join(str(el) for el in num_list[::-1])


def convert_bin_dec(input_number):
    decimal_num = 0
    input_list = list(str(input_number))[::-1]
    pow_counter = 0
    for digit in input_list:
        if digit == '1':
            decimal_num += 2**pow_counter
        pow_counter += 1
    return decimal_num


def convert_number(input_number, from_system, to_system):
    if from_system == 10 and to_system == 2:
        return convert_dec_bin(input_number)
    if from_system == 2 and to_system == 10:
        return convert_bin_dec(input_number)
    return 'OOOOps, there is a mistake'


num = int(input())
print('Binary:', convert_number(num, 10, 2))
print('Decimal:', convert_number(convert_number(num, 10, 2), 2, 10))
