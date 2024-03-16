import heapq

a = int(input())
card_list = []
for i in range(a):
    card_list.append(int(input()))
card_list.sort(reverse=False)

cnt = 0
if len(card_list) == 1:
    print(cnt)
else:
    for j in range(a -1):
        first_low = heapq.heappop(card_list)
        second_low = heapq.heappop(card_list)
        
        cnt += first_low + second_low
        heapq.heappush(card_list, first_low + second_low)

print(cnt)