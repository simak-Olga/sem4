#задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def natural number(n):
   i = 2
   natural number = []
   while i * i <= n:
       while n % i == 0:
           natural number.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       natural number.append(n)
   return natural number