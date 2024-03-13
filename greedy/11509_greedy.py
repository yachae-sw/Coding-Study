balloon_number = int(input())
balloon_space = list(map(int, input().split()))

flag = [0] * 1000001 ##리스트로 생성

cnt = 0
for i in range(balloon_number):
    if flag[balloon_space[i]] == 0: ## 초기값 위치 설정
        cnt = cnt + 1
        flag[balloon_space[i] - 1] += 1 ## 그 다음 풍선 자동으로 터짐
    else: ## 풍선 자동으로 터지는 위치라면
        flag[balloon_space[i]] -= 0 ## 그 위치는 다시 초기화 
        flag[balloon_space[i] - 1] += 1 ## 그 다음 풍선 자동으로 터짐
            
print(cnt)
