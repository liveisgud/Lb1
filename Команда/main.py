# Функция для вычисления суммы двух чисел
def add(a, b):
    return a + b

# Функция для вычисления разности двух чисел
def subtract(a, b):
    return a - b

# Функция для определения четности числа
def is_even(num):
    return num % 2 == 0

# Функция для вычисления факториала числа
def factorial(n):
    if n == 0:
        return 1
        return n * factorial(n-1)