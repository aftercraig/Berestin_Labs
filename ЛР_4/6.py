s = input("Введите строку: ")
lowercase = sum(1 for c in s if c.islower())
uppercase = sum(1 for c in s if c.isupper())
print(f"Маленькие буквы: {lowercase}, Большие буквы: {uppercase}")