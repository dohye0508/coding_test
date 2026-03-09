'''
벨만-포드 알고리즘 (Bellman-Ford)
가중치 그래프에서 시작 노드로부터 다른 모든 노드까지의 최단 경로를 구하되, '음수 간선'이 포함되어 있어도 처리할 수 있는 알고리즘.
시간 여행, 혹은 적자/흑자가 반복되는 코스에서 음수 사이클(계속 이익이 복사되는 무한 루프)이 존재하는지 판별할 때 주로 사용.

[입력 예시]
노드의 개수 N, 간선의 개수 M
M개의 줄에 걸쳐 간선 정보 A B C (A에서 B로 가는데 비용이 C, 음수 가능)
'''
import sys

INF = int(1e9)

n, m = map(int, sys.stdin.readline().split())
edges = []
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((a, b, c))

def bf(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]
            
            if dist[cur_node] != INF and dist[next_node] > dist[cur_node] + edge_cost:
                dist[next_node] = dist[cur_node] + edge_cost
                if i == n - 1:
                    return True
    return False

negative_cycle = bf(1)

if negative_cycle:
    print("-1")
else:
    for i in range(2, n + 1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])
