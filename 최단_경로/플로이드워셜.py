'''
플로이드 워셜 (Floyd-Warshall)
모든 지점에서 다른 모든 지점까지의 최단 경로를 구하는 알고리즘입니다. 노드의 개수가 적을 때 효율적입니다.
시간 복잡도: O(N^3)

[입력 예시]
첫 줄에 노드의 개수(N), 두 번째 줄에 간선의 개수(M)를 입력합니다.
그 다음 줄부터 M개의 줄에 걸쳐 간선 정보(출발, 도착, 비용)를 입력합니다.
'''
import sys

INF = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
