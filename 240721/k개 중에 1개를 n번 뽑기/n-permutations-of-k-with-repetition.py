import sys

k, n = map(int, sys.stdin.readline().split())

arr = []


def dfs(cnt):
    if cnt == n:
        print(*arr)
        return

    for i in range(1, k + 1):
        arr.append(i)
        dfs(cnt + 1)
        arr.pop()


dfs(0)