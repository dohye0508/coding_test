'''
행렬 곱셈 순서 (Matrix Chain Multiplication) - DP
N개의 행렬을 연속해서 곱할 때, 어떤 순서로 괄호를 묶어 곱셈을 하느냐에 따라 연산 횟수가 달라집니다.
최소의 곱셈 연산 횟수를 구하는 2차원 구간 DP의 대표적인 사례입니다.
구간의 길이 L을 1부터 N-1까지 늘려가며 탐색하고,
i부터 k까지의 최소 횟수 + k+1부터 j까지의 최소 횟수 + 앞뒤 결과 행렬을 합치는 비용을 계산합니다.

[입력 예시]
행렬의 개수 N
N개의 줄에 걸쳐 각 행렬의 크기 r, c (행과 열)
(단, i번째 행렬의 열과 i+1번째 행렬의 행의 크기는 같습니다.)
'''
import sys

n = int(sys.stdin.readline())
matrices = []
for _ in range(n):
    r, c = map(int, sys.stdin.readline().split())
    matrices.append((r, c))

dp = [[0] * n for _ in range(n)]

for L in range(1, n):
    for i in range(n - L):
        j = i + L
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + matrices[i][0] * matrices[k][1] * matrices[j][1]
            if cost < dp[i][j]:
                dp[i][j] = cost

print(dp[0][n-1])
