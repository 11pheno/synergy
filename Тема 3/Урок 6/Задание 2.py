a = int(input("Введите натуральное число:"))
n = 0
count = 0

while n < a:
    n += 1
    if (a % n) == 0:
        count += 1

print("Количество натуральных делителей числа:", count)
