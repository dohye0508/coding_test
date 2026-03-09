'''
동전 교환 문제 (Coin Change)
N가지 종류의 동전이 주어질 때, 이 동전들을 이용해 목표 금액 K를 만드는 경우의 수, 혹은 최소 동전 사용 개수를 구하는 알고리즘.
가장 적은 화폐로 거스름돈을 줄 때 등에서 사용.

[입력 예시]
동전의 종류 N, 만들고자 하는 금액 K
N개의 줄에 걸쳐 각 동전의 액면가 입력
'''
import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

dp = [int(1e9)] * (k + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        if dp[i - coin] != int(1e9):
            dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[k] == int(1e9):
    print(-1)
else:
    print(dp[k])
