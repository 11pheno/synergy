n1 = list(map(int, input('Введите первый список чисел:').split()))
n2 = list(map(int, input('Введите второй список чисел:').split()))
nl1 = set(n1)
nl2 = set(n2)
print(len(nl1.intersection(nl2)))