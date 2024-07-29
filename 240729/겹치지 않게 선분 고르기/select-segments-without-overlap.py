import sys

n = int(sys.stdin.readline())

lines = []

for i in range(n):
    lines.append(list(map(int, sys.stdin.readline().split())))

num = [0] * 1001

ans = 0
reach_max = False


def dfs(idx, cnt):

    global n, ans, reach_max, num, lines
    if cnt == n or reach_max:
        ans = n
        reach_max = True
        return

    for i in range(idx + 1, len(lines)):
        start = lines[i][0]
        end = lines[i][1]

        if 0 in num[start : end + 1]:
            num[start : end + 1] = [1] * (end - start + 1)
            dfs(i, cnt + 1)
            num[start : end + 1] = [0] * (end - start + 1)

    ans = max(ans, cnt)


dfs(-1, 0)


print(ans)