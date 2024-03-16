import sys

N = int(sys.stdin.readline())

count = [int(sys.stdin.readline()) for _ in range(N)]

count.sort(reverse=True)

result = []
for i in range(N):
    result.append(count[i]*(i+1))

print(max(result))