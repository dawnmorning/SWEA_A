import sys
input = sys.stdin.readline
c, r = map(int, input().split())
k = int(input())
seat = [[0] * c for _ in range(r)]
if k > r * c:
    print(0)
    sys.exit()
current_r = r-1
current_c = 0
cnt = 1
dir = 0
dr = [-1,0,1,0]
dc = [0,1,0,-1]
while True:
    if cnt == k:
        print(current_c+1, r-current_r)
        break
    seat[current_r][current_c] = cnt
    nr = current_r + dr[dir]
    nc = current_c + dc[dir]
    if nr < 0 or nc < 0 or nr >= r or nc >=c or seat[nr][nc] != 0:
        dir = (dir + 1) % 4
        nr = current_r + dr[dir]
        nc = current_c + dc[dir]

    current_r = nr
    current_c = nc
    cnt += 1
