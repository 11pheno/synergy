
cycles = int(input("Введите количество чисел:"))
count = 0

for i in range(cycles):
    number = int(input("Введите число:"))
    if number == 0:
        count += 1
print("Количество чисел равных нулю:", count)

