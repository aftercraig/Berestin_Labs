D = [4, 3, 7, 8, 2, 5]
sum_odd_indices = sum(D[i] for i in range(1, len(D), 2))
print("Список D:", D)
print("Сумма элементов с нечётными индексами:", sum_odd_indices)