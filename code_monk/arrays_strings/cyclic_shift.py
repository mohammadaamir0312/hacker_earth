T = int(input())
while T > 0:
    N, K = map(int, input().split())
    s = input()
    i = 1
    maxCount = 0
    maxPos = []
    if s[0] == s[N-1] and s[0] == '1':
        i = N - 1
        count = 0
        while i >= 0 and s[i] == '1':
            i -= 1
            count += 1
        if i == -1:
            print(0)
            continue
        maxPos = [i + 1]
        i = 0
        while i < N and s[i] == '1':
            i += 1
            count += 1
        maxCount = count
    while i < N:
        while i < N and s[i] =='0':
            i += 1
        if i == N:
            print(0)
        count = 1
        pos = i
        while i < N-1 and s[i] == s[i+1]:
            count += 1
            i += 1
        if count > maxCount:
            maxCount = count
            maxPos = [pos]
        elif count == maxCount:
            maxPos.append(pos)
        i += 1
    rounds = K / len(maxPos)
    if len(maxPos) == 0 or K == 0:
        print(0)
    else:
        print(maxCount)
        print(maxPos)
        ans = maxPos[0]
        K -= 1
        rounds = K // len(maxPos)
        ans += N * rounds
        rem = K - rounds * len(maxPos)
        prev = maxPos[0]
        print(rounds, ans, prev, rem)
        for i in range(rem):
            ans += maxPos[i + 1] - prev
            prev = maxPos[i + 1]
        print(ans)
    T -= 1