min_fund = int(input())
Mike = int(input())
Ivan = int(input())

if (Mike >= min_fund) and (Ivan >= min_fund):
    print(2)
elif (Mike >= min_fund) or (Ivan >= min_fund) or ((Mike + Ivan) >= min_fund):
    print(1)
elif ((Mike + Ivan) < min_fund):
    print(0)
