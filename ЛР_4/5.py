s = input("Введите строку слов: ")
longest = max(s.split(), key=len)
print(f"Самое длинное слово: {longest}")