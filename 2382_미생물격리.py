tc = int(input())

for t in range(1,tc+1):
    tbl=[0,2,1,4,3]
    di, dj = [0,-1,1,0,0], [0,0,0,-1,1]
    n,m,k = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(k)]

    for _ in range(m):
        # 1칸 이동, 경계면이면 //2 , 방향 반대로 바꾸기
        for i in range(len(arr)):
            # [0]: i, [1]:j, [2]:n, [3]:dr
            arr[i][0] = arr[i][0] + di[arr[i][3]] # 세로 위치 이동
            arr[i][1] = arr[i][1] + dj[arr[i][3]] # 가로 위치 이동
            # 이동 후 경계면이라면
            if arr[i][0] == 0 or arr[i][0] == n-1 or arr[i][1] == 0 or arr[i][1] == n-1:
                arr[i][2] //= 2
                # 반대 방향으로 전환
                arr[i][3] = tbl[arr[i][3]]
        
        # 내림차순 정렬, 큰 놈으로 합쳐지니까
        arr.sort(key=lambda x : (x[0],x[1],x[2]),reverse=True)
        # 같은 곳 합치기
        i=1
        while i < len(arr):
            # i ,j 같은 경우에 합친다
            if arr[i-1][0:2] == arr[i][0:2]:
                arr[i-1][2] += arr[i][2]
                arr.pop(i)
            else:
                i += 1
    ans = 0
    for lst in arr:
      ans += lst[2]  
    print(f'#{t} {ans}')
            