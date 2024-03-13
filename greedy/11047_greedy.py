N, K = map(int, input().split())

## 동전 형태 생성
coin_list = []
for i in range(N):
    coin_list.append(int(input()))
coin_list.sort(reverse=True) # 값이 큰 동전을 먼저 사용하기 위해 정렬

result = 0
for coin in coin_list:
    if K >= coin:
        result += K // coin # 몫만 저장
        K %= coin # k 값을 나머지로 할당
        if K <= 0:
       		break
print(result)