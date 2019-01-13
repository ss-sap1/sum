'''считывает с ввода целые числа, по одному числу в строке, и после первого введенного нуля выводит сумму полученных на вход чисел'''

number = int(input())
summ = 0
while number != 0:
    summ = number + summ
    number = int(input())
print(summ)