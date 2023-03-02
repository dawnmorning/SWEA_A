import sys
sys.stdin = open('4012.txt')

def dfs(a, alst, blst):
    global ans
    # 4개가 되고
    if a == n:
        # 길이가 반토막이면
        if len(alst) == m:
            # 시작
            asum = bsum = 0
            for i in range(m):
                for j in range(m):
                    # 인덱스 조합을 통한 값들 넣기
                    asum += arr[alst[i]][alst[j]]
                    bsum += arr[blst[i]][blst[j]]
            ans = min(ans, abs(asum-bsum))
        return
    dfs(a+1, alst+[a], blst)
    dfs(a+1, alst, blst+[a])


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    m = n//2
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 20000 ** n
    dfs(0,[],[])
    print(f'#{tc} {ans}')