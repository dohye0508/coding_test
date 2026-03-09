'''
KMP 문자열 매칭 (Knuth-Morris-Pratt Algorithm)
긴 문장 속에서 특정 문자열(패턴)을 찾을 때, 접두사와 접미사 개념(LPS 배열)을 이용해 불필요한 비교를 건너뛰며 O(N+M)의 시간으로 빠르게 검색하는 알고리즘.

[입력 예시]
원본 긴 문자열
찾고자 하는 패턴 문자열
'''
import sys

text = sys.stdin.readline().strip()
pattern = sys.stdin.readline().strip()

t_len = len(text)
p_len = len(pattern)

lps = [0] * p_len
match_idx = 0

for i in range(1, p_len):
    while match_idx > 0 and pattern[i] != pattern[match_idx]:
        match_idx = lps[match_idx - 1]
    if pattern[i] == pattern[match_idx]:
        match_idx += 1
        lps[i] = match_idx

matches = []
match_idx = 0

for i in range(t_len):
    while match_idx > 0 and text[i] != pattern[match_idx]:
        match_idx = lps[match_idx - 1]
    if text[i] == pattern[match_idx]:
        if match_idx == p_len - 1:
            matches.append(i - p_len + 2)
            match_idx = lps[match_idx]
        else:
            match_idx += 1

print(len(matches))
for m in matches:
    print(m, end=' ')
