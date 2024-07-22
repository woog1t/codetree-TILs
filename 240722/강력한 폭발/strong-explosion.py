import sys

n = int(sys.stdin.readline())

mat = []
for i in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))

bomb = []

for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            bomb.append([i, j])


dc = [
    [[1, 0], [2, 0], [-1, 0], [-2, 0]],
    [[1, 0], [-1, 0], [0, 1], [0, -1]],
    [[1, 1], [1, -1], [-1, -1], [-1, 1]],
]

ans = 0


def dfs(cur):
    global ans, mat, dc
    if cur == len(bomb):
        sum = 0
        for i in range(n):
            for j in range(n):
                if mat[i][j] != 0:
                    sum += 1
        ans = max(ans, sum)
        return

    x = bomb[cur][0]
    y = bomb[cur][1]

    for i in range(0, 3):
        for j in range(0, 4):
            nx = x + dc[i][j][0]
            ny = y + dc[i][j][1]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            mat[nx][ny] += 1

        dfs(cur + 1)

        for j in range(0, 4):
            nx = x + dc[i][j][0]
            ny = y + dc[i][j][1]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            mat[nx][ny] -= 1


dfs(0)

print(ans)