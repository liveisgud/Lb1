<<<<<<< .merge_file_eadrfV
# Функция для вычисления суммы двух чисел
def add(a, b):
    return a + b
=======
# Функция для вычисления разности двух чисел
def subtract(a, b):
    return a - b

# Функция для вычисления произведения двух чисел
def multiply(a, b):
    return a * b
>>>>>>> .merge_file_TFzLlT

# Функция для вычисления произведения двух чисел
def multiply(a, b):
    return a * b

# Функция для вычисления частного двух чисел
def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
        return a / b


# Функция для проверки простого числа
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
            return True


# Функция для нахождения минимального числа из списка
def find_min(nums):
    return min(nums)
