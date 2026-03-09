'''
편집 거리 알고리즘 (Edit Distance / Levenshtein Distance)
두 문자열이 완전히 같아지기 위해 문자열에 대해 최소 몇 번의 삽입, 삭제, 교체 연산이 필요한지 구하는 알고리즘.
검색어 자동완성, 철자 교정 프로그램, 생물정보학(염기서열 유사성) 등에 사용.

[입력 예시]
바꾸고자 하는 원본 문자열 A
목표 문자열 B
'''
import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

n = len(s1)
m = len(s2)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = i
for j in range(1, m + 1):
    dp[0][j] = j

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

print(dp[n][m])
