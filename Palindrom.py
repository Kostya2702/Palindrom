number = int(input('Введите любое целое число: '))

def palindrom(number):
    result = 0
    while (number > 0):
        result = result * 10 + number % 10
        number //= 10
        
    return result

if palindrom(number) == number:
    print('Это палиндром')
else:
    print('Попробуйте заново')



