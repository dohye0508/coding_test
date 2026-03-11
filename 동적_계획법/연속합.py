'''
연속합 (Maximum Subarray)
주어진 수열에서 임의의 연속된 일부 구간의 수를 모두 더했을 때 얻을 수 있는 최대합을 구하는 알고리즘.
주식의 최대 수익 구간 찾기, 시계열 데이터 중 구간의 최대 상승 폭 찾기 등에서 사용.

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
arr = list(map(int, sys.stdin.readline().split()))

dp = [0] * n
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(arr[i], dp[i - 1] + arr[i])

print(max(dp))
