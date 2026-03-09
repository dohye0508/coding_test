'''
다익스트라 (Dijkstra)
양의 가중치 간선이 있는 그래프에서 단일 출발점 최단 경로를 구하는 알고리즘입니다. 우선순위 큐를 사용합니다.
시간 복잡도: O(E log V)

[입력 예시]
노드의 개수(N)와 간선의 개수(M)를 입력하고, 시작 노드를 입력합니다.
그 다음 줄부터 M개의 줄에 걸쳐 간선 정보(출발, 도착, 비용)를 입력합니다.
'''
import heapq
import sys

INF = int(1e9)

def dijkstra(start, graph, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n, m = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

dijkstra(start, graph, distance)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
