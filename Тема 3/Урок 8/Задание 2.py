n = int(input())
res = list(map(int, input().split()))[:n]

res.insert(0, res.pop())
# под 0 индекс массива res вставляем последнее число массива через .pop
print(res)