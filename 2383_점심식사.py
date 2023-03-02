def dfs(a, alst, blst):
    global ans
    if a == n:
        if len(alst) == m:
            asum = bsum = 0
            for i in range(m):
                for j in range(m):
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