numbers = [4, -3, 7, -1, 0, 5]
positive_numbers = [x for x in numbers if x > 0]
other_numbers = [x for x in numbers if x <= 0]
print("Положительные:", positive_numbers)
print("Остальные:", other_numbers)