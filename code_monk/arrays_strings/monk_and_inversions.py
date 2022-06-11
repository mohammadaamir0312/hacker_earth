T = int(input())
while T > 0:
    N = int(input())
    M = []
    inversions = 0
    for i in range(N):
        M.append(list(map(int, input().split())))
    for i in range(N):
        for j in range(N):
            for k in range(i, N):
                for l in range(j, N):
                    if M[i][j] > M[k][l]:
                        inversions += 1
    print(inversions)
    T -= 1