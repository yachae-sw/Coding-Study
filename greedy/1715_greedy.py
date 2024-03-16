import heapq
import sys

a = int(sys.stdin.readline())
card_list = []
for i in range(a):
    input_num = int(sys.stdin.readline())
    heapq.heappush(card_list,input_num)

cnt = 0
while len(card_list) != 1:
    for j in range(a -1):
        first_low = heapq.heappop(card_list)
        second_low = heapq.heappop(card_list)

        cnt += first_low + second_low
        heapq.heappush(card_list, first_low + second_low)

print(cnt)