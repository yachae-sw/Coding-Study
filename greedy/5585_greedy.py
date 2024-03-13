coin_list = [500, 100, 50, 10, 5, 1]

m = 1000 - int(input())

result = 0
for coin in coin_list:
    result += m // coin
    m %= coin


print(result)