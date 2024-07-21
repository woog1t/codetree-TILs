import sys

n, m = map(int, sys.stdin.readline().split())
mat = []

for i in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))

ans = 0

# ㄴ-정방향
for i in range(1, n):
    for j in range(m - 1):
        sum = mat[i][j] + mat[i - 1][j] + mat[i][j + 1]
        ans = max(ans, sum)

# ㄴ-뒤집기
for i in range(1, n):
    for j in range(1, m):
        sum = mat[i][j] + mat[i - 1][j] + mat[i][j - 1]
        ans = max(ans, sum)

# ㄱ-정방향
for i in range(n - 1):
    for j in range(1, m):
        sum = mat[i][j] + mat[i + 1][j] + mat[i][j - 1]
        ans = max(ans, sum)

# ㄱ-뒤집기
for i in range(n - 1):
    for j in range(m - 1):
        sum = mat[i][j] + mat[i + 1][j] + mat[i][j + 1]
        ans = max(ans, sum)

# -
for i in range(n):
    for j in range(1, m - 1):
        sum = mat[i][j] + mat[i][j - 1] + mat[i][j + 1]
        ans = max(ans, sum)

# ㅣ
for i in range(1, n - 1):
    for j in range(m):
        sum = mat[i][j] + mat[i - 1][j] + mat[i + 1][j]
        ans = max(ans, sum)

print(ans)