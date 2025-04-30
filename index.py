def fizz_buzz(begin, end):
    result = ''
    for i in range(begin, end + 1):
        if result != '':
            result = result + ' '

        if i % 3 == 0 and i % 5 == 0:
            result = result + 'FizzBuzz'
        elif i % 3 == 0:
            result = result + 'Fizz'
        elif i % 5 == 0:
            result = result + 'Buzz'
        elif begin > end:
            result = ''
        else:
            result = result + str(i)
    return result

# Проверка

begin = 1
end = 5

print(fizz_buzz(begin, end))