# задача 1. Напишите код, который вычисляет факториал введенного числа
# x = int(input('Введите число: '))
# fact = 1
# while x>0:
#     fact *= x
#     x -= 1
# print(fact)

# задача 2. Дано число А>1, поределите каким по счёту оно является в ряду Фибоначчи
# x = int(input('Введите число: '))
# num1 = 0
# num2 = 1
# num3 = 0
# isFib = False
# i = 2
# while num3 < x:
#     num3 = num1 + num2
#     num1 = num2
#     num2 = num3
#     i += 1
#     print(num3)
#     if num3 == x:
#         isFib = True
# if isFib:
#     print(i)
# else:
#     print(-1)