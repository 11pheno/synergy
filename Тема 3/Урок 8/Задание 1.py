n = int(input())
res = []
for i in range(n):
    a = int(input())
    if a >= 1 and a <= 10000:
        res.append(a)
res.reverse()
print(res)