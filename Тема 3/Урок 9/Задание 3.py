tmp = set()

for i in input('Введите последовательность чисел:').split():
    if i not in tmp:
         tmp.add(i)
         print('NO')
    else:
        print('YES')