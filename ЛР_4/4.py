s = input("Введите два слова через пробел: ")
words = s.split()
if len(words) >= 2:
    print(f"Второе слово: {words[1]}")
else:
    print("Ошибка: нужно два слова.")