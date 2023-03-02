# 두 일꾼, 각각 연속된 N개(겹침 X)
# 선택된 M개 이익 최대.. 아니라면 더 가지말고 백트래킹

def dfs(start,cnt,temp_sum,current_r, current_c):
    global maxV
    # 최대 양보다 크면 return
    if cnt > c:
        return
    
    # 다 돌았을 때
    if n == m:
        maxV = max(maxV, temp_sum)
        return
    # 벌통 채취하면
    dfs(start+1, cnt+honey_box[current_r][current_c+start], temp_sum+honey_box[current_r][current_c+start] ** 2, current_r,current_c)
    # 안 하면
    dfs(start+1, cnt,temp_sum, current_r,current_c)

t = int(input())
for tc in range(1,t+1):
    n, m, c = map(int, input.split())
    honey_box = [list(map(int, input().split)) for _ in range(n)]
    ans = maxV = temp_sum = 0
    # 가능한 모든 시작 위치

    # 일꾼 1
    for i in range(n):
        for j in range(n-m+1):
            maxV = 0
            dfs(0,0,0,i,j)
            temp_sum = maxV
            # 일꾼 2
            for k in range(i, n):
                # 일꾼 2는 행이 같으면 일꾼 1이 가지 않은 곳에서 시작. 
                start_2 = j + m if i==k else 0
                for l in range(start_2, n-m+1):
                    maxV = 0
                    dfs(0,0,0,k,l)
                    ans = max(ans, temp_sum+maxV)
    print(f'#{tc} {ans}')
