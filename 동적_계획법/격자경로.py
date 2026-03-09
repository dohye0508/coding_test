'''
2차원 격자 이동 DP (Grid Path DP)
N x M 크기의 격자 형태 미로에서 이동 제약 조건(예: 오른쪽이나 아래로만 이동 가능)이 있을 때 도달하는 최소 비용, 혹은 가능한 경로의 수를 찾는 알고리즘.
특정 칸에 장애물이 있거나 각 칸마다 밟았을 때 얻는/잃는 점수가 다를 때 최대/최소 이득 수치를 산출함.

[입력 예시]
격자의 세로 N, 가로 M
N개의 줄에 걸쳐 각 칸에 해당하는 점수/비용 수치 입력
'''
import sys

n, m = map(int, sys.stdin.readline().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().split())))

dp = [[0] * m for _ in range(n)]
dp[0][0] = grid[0][0]

for i in range(1, m):
    dp[0][i] = dp[0][i - 1] + grid[0][i]

for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + grid[i][0]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = grid[i][j] + max(dp[i - 1][j], dp[i][j - 1])

print(dp[n - 1][m - 1])
