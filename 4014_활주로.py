def stiff(array):
    length = 1
    for i in range(1,n):
        # 같은 높이
        if array[i] == array[i-1]: 
            length += 1
        # 1 높아지는 경우
        elif array[i] - array[i-1] == 1 and length >= x:
            length = 1
        # 1 낮아지는 경우
        elif array[i-1] - array[i] == 1 and length >= 0:
            length = -x + 1
        # 그거 아니면
        else:
            return 0
    # 살아 남았니
    if length >= 0:
        return 1
    else:

        return 0

t = int(input())
for tc in range(1, t+1):
    n, x = map(int,input().split())
    plain_area = [list(map(int,input().split())) for _ in range(n)]
    answer = 0
    for i in range(n):
        answer += stiff(plain_area[i])
    for i in range(n):
        shuffle = []
        for j in range(n):
            shuffle.append(plain_area[j][i])
        answer += stiff(shuffle)
    print(f'#{tc} {answer}')

