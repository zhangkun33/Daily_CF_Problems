# Submission link: https://codeforces.com/contest/492/submission/255590031
n, x, y = map(int, input().split())
ans = []
for _ in range(n):
    v = int(input())
    l, r = 0, 10 **15
    while l < r:
        mid = l + r >> 1
        if mid // x + mid // y >=v:
            r = mid
        else:
            l = mid + 1
    if l % x == 0:
        if l % y == 0:
            ans.append('Both')
        else:
            ans.append('Vova')
    else:
        ans.append('Vanya')
print('\n'.join(ans))