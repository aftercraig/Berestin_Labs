n = int(input("Введите количество чисел: "))
fib = [1, 1]
for _ in range(2, n):
    fib.append(fib[-1] + fib[-2])
print(fib[:n])