'''
0/1 배낭 문제 (Knapsack Problem)
각 물건의 무게와 가치가 주어졌을 때, 견딜 수 있는 배낭의 최대 무게 내에서 담을 수 있는 가치의 합의 최댓값을 구하는 알고리즘.
특정 상황(물건을 쪼갤 수 없는 상황)에서 가장 높은 효율을 내야 할 때 사용.

[입력 예시]
물품의 수 N, 버틸 수 있는 최대 무게 K
N개의 줄에 걸쳐 각 물건의 무게 W와 가치 V 입력
'''
import sys

n, k = map(int, sys.stdin.readline().split())
items = []
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    items.append((w, v))

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    w, v = items[i - 1]
    for j in range(1, k + 1):
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[n][k])
