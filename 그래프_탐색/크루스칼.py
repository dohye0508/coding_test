'''
크루스칼 알고리즘 (Kruskal's Algorithm) - 최소 신장 트리 (MST)
그래프 내의 모든 노드를 포함하면서 사이클이 없고, 간선 가중치의 합이 최소가 되는 트리를 찾는 알고리즘.
모든 마을을 최소 비용으로 연결하는 전력망 구축 등에 사용.

[입력 예시]
노드의 개수 V, 간선의 개수 E
E개의 줄에 걸쳐 간선 정보 A B C (A와 B를 연결하는 가중치 C)
'''
import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, sys.stdin.readline().split())
parent = [0] * (v + 1)
edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
