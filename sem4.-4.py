#задача 4. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
def numbers(a, b):
    if a < b:
        return numbers(b, a)
    if a == 0 or b == 0:
        return a | b
    return numbers(b, a % b)
 
a, b = map(int, input().split(maxsplit=1))
print(a * b // numbers(a, b))
