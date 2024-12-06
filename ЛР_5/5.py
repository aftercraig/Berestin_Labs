numbers = [12, 20, 8, 15, 22, 14, 7, 30]
modified_numbers = [x * 2 if x < 15 else x for x in numbers]
print("Преобразованный массив:", modified_numbers)