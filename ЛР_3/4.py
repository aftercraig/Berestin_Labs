import random
number = random.randint(1, 100)
while True:
    guess = input("Угадайте число или введите 'exit' для выхода: ")
    if guess.lower() == 'exit':
        break
    guess = int(guess)
    if guess > number:
        print("Загаданное число меньше.")
    elif guess < number:
        print("Загаданное число больше.")
    else:
        print("Вы угадали!")
        break