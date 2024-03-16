import sys
 
N = int(sys.stdin.readline())
list_plus = []
for _ in range(N):
    a = str(sys.stdin.readline())
    list_plus.append(len(a))
    print(list_plus)