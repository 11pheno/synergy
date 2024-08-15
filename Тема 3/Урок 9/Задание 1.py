n = int(input())
n1 = list(map(int, input().split()))[:n]
tmp = set(n1)
print(len(tmp))