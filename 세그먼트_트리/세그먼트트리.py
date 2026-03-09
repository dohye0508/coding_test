'''
세그먼트 트리 (Segment Tree) - 비재귀(Iterative) 방식
주어진 배열에서 특정 구간의 합/최솟값/최댓값을 빠르게 O(log N) 시간에 처리하는 자료구조 및 알고리즘입니다.

[입력 예시]
데이터 개수 N, 변경 횟수 M, 구간 합 구하는 횟수 K 입력
이후 N개의 배열 요소, 그리고 M+K개의 쿼리가 주어집니다.
'''
import sys

class SegTree:
    def __init__(self, data, n):
        self.n = n
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            if i % 2 == 0:
                self.tree[i // 2] = self.tree[i] + self.tree[i + 1]
            else:
                self.tree[i // 2] = self.tree[i - 1] + self.tree[i]
            i //= 1

    def query(self, l, r):
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 1:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res

input_data = sys.stdin.read().split()
if input_data:
    n = int(input_data[0])
    arr = list(map(int, input_data[1:n+1]))
    st = SegTree(arr, n)
