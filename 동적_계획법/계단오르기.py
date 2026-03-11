'''
계단 오르기 (Climbing Stairs) - 1D DP
n개의 계단을 오르는데, 한 번에 1계단 또는 2계단씩 오를 수 있으며 연속된 세 개의 계단을 모두 밟을 수는 없는 조건일 때,
얻을 수 있는 총 점수의 최댓값을 구하는 매우 유명한 기초 DP입니다.

[입력 예시]
5 3
1 2
2 3
3 4
4 5

[출력 예시]
1
2
3 4 5
'''
import sys

n = int(sys.stdin.readline())
stairs = [0] * 301

for i in range(n):
    stairs[i] = int(sys.stdin.readline())

dp = [0] * 301

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2])

for i in range(3, n):
    dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])

print(dp[n - 1] if n > 0 else 0)
