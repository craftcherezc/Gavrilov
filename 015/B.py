import random


def is_p(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        return True


ar_A = [random.randint(0, 100) for _ in range(5)]
print("Массив A:")
print(*ar_A)

ar_B = [num for num in ar_A if is_p(num)]
print("Массив B:")
print(*ar_B)
