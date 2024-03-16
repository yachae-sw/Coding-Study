import math

A, B, V = map(int,input().split())

c = (V - B) / (A - B)
print(math.ceil(c))