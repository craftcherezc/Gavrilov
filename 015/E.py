import random

ar = [random.randint(1, 6) for _ in range(6)]
print("Массив:")
print(*ar)

mid = len(ar) // 2
ar[:mid] = ar[:mid][::-1]
ar[mid:] = ar[mid:][::-1]
print("РЕЗУЛЬТАТИЩЕ:")
print(*ar)
