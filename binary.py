user_input = input('Please enter a number and numeral system of that number separated by space (1234 10): ')

split_user_input = user_input.split()

number = int(split_user_input[0])

number_system = int(split_user_input[1])


def bin_dec_conversion(number, number_system):

    if number_system == 10:

        binary_reversed = ''

        while number > 0:
            remainder = number % 2
            binary_reversed += str(remainder)
            number = number // 2

        if len(binary_reversed) < 16:
            for i in range(16-len(binary_reversed)):
                binary_reversed += '0'

        binary = (f'{binary_reversed[::-1]} 2')

        return binary

    elif number_system == 2:

        binary_number = (str(number))[::-1]

        decimal_number = 0

        for i in range(len(binary_number)):
            if binary_number[i] == '1':
                decimal_number += 2**i

        decimal = (f'{decimal_number} 10')

        return decimal

    else:
        print('invalid number system')


print(bin_dec_conversion(number, number_system))
