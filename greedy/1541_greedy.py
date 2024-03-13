n = str(input())
m = n.split('-') # -를 기준으로 괄호를 삽입하면 최솟값 도출이 가능하다

result = 0

a = sum(map(int, (m[0].split('+')))) # +를 기준으로 값 저장(첫번째 수식에 -가 있을경우)
if n[0] == '-':
    result -= a
else:
    result += a

for i in m[1:]: # -로 split된 값들을 안에 있는 + 작업을 한 후 최종 결과만 -로 적용
    b = sum(map(int, (i.split('+')))) # +를 기준으로 값 저장
    result -= b

print(result)