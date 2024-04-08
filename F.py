import random

ar = [random.randint(-100, 100) for _ in range(6)]
print("Массив:")
print(*ar)

pos_elem = [num for num in ar if num > 0]
neg_elem = [num for num in ar if num <= 0]
ar = pos_elem + neg_elem
print("РЕЗУЛЬТАТИЩЕ:")
print(*ar)
print("Количество положительных элементов:", len(pos_elem))
