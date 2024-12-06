import random
number = random.randint(0, 100)
attempts = 0
while attempts < 10:
    guess = int(input("Угадайте число: "))
    attempts += 1
    if guess == number:
        print("Вы угадали!")
        break
    elif guess > number:
        print("Загаданное число меньше.")
    else:
        print("Загаданное число больше.")
if attempts == 10 and guess != number:
    print(f"Вы проиграли! Загаданное число было: {number}")