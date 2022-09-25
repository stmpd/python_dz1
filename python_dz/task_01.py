#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
#и проверяет, является ли этот день выходным.
#*Пример:*
#- 6 -> да
#- 7 -> да
#- 1 -> нет

a = int(input('Введите день недели:'))
if a > 0 and a <= 5:
    print('Workday')
elif (a == 6 or a == 7):
    print('Weekend')
else:
    print('Such day of the week does not exist')