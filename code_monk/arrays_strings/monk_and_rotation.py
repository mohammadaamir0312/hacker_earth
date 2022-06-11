T = int(input())
while T > 0:
    N, K = map(int, input().split())
    arr = list(input().split())
    i = 0
    K = N - K % N
    while i < N:
        print(arr[(i + K) % N] + ' ', end='')
        i += 1
    print()
    T -= 1