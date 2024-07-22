import sys

n = int(sys.stdin.readline())


num = [0] * 5
ans = 0

arr = []


def beautiful_check(arr: list):
    cnt = 1
    for i in range(1, len(arr)):
        if arr[i - 1] == arr[i]:
            cnt += 1
        else:
            if cnt % arr[i - 1] != 0:
                return False
            cnt = 1
    if cnt % arr[len(arr) - 1] != 0:
        return False
    return True


def dfs(cnt):
    global ans, arr
    if cnt == n:
        if beautiful_check(arr) == True:
            ans += 1
        return

    for i in range(1, 5):
        arr.append(i)
        dfs(cnt + 1)
        arr.pop()


dfs(0)
print(ans)