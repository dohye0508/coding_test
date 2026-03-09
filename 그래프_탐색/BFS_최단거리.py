'''
너비 우선 탐색 (BFS) - 최단거리
큐를 이용하여 그래프의 인접한 노드부터 먼저 탐색하는 알고리즘입니다. 최단 경로 탐색에 주로 사용됩니다.
가까운 노드부터 탐색하여, 간선의 비용이 동일할 때 최단 거리를 구합니다.
시간 복잡도: O(V + E)

[입력 예시]
세로 길이(N)와 가로 길이(M)를 입력하고, 그 다음 줄부터 N개의 줄에 거쳐 미로 맵 정보를 입력합니다. (예: 101010)
'''
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, n, m, graph):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    return graph[n - 1][m - 1]

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(sys.stdin.readline().rstrip()))))

if graph[0][0] == 1:
    print(bfs(0, 0, n, m, graph))
else:
    print("Not Valid Start")
