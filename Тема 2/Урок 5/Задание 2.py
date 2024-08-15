word = input('Введите слово маленькими буквами на латинице:')
glasnie = 0
soglasnie = 0

for letter in word:
    if letter in "aeiou":
        glasnie += 1
    elif letter in "bcdfghjklmnpqrstvwxyz":
        soglasnie += 1
    else:
        print(False)

print('Количество гласных букв в слове', word, ":", glasnie)