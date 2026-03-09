'''
회의실 배정 (Activity Selection / Greedy)
시작 시간과 끝나는 시간이 정해진 N개의 회의가 주어질 때, 겹치지 않게 하면서 가장 많은 회의를 할 수 있는 개수를 구하는 알고리즘.
그리디 알고리즘의 대표적인 예시로, '끝나는 시간'을 기준으로 오름차순 정렬하는 것이 핵심입니다.

[입력 예시]
회의의 개수 N
N개의 줄에 걸쳐 각 회의의 시작 시간과 종료 시간
'''
import sys

n = int(sys.stdin.readline())
meetings = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
current_end_time = 0

for start, end in meetings:
    if start >= current_end_time:
        current_end_time = end
        count += 1

print(count)
