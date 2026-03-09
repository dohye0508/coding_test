'''
유니온 파인드 (Union-Find)
서로소 집합을 표현하는 자료구조로, 노드 연결(Union)과 공통 조상 찾기(Find) 연산을 지원합니다. 무방향 그래프의 사이클 판별에 주로 사용됩니다.
여러 노드가 있을 때 서로 같은 그래프에 속하는지 판별하는 알고리즘.

[입력 예시]
노드의 개수(V)와 간선의 개수(E)를 입력하고, 다음 E개의 줄에 걸쳐 연결된 두 노드를 입력합니다.
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

for i in range(1, v + 1):
    parent[i] = i

cycle = False
for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print("Cycle Exists")
else:
    print("No Cycle")
