'''
에라토스테네스의 체 (Sieve of Eratosthenes)
어떤 수 N이하의 모든 소수를 빠르고 효율적으로 찾는 수학 알고리즘입니다.
소수가 아닌 수들의 배수를 지워나가는 방식으로 동작하며 O(N log(log N))의 매우 빠른 속도를 자랑합니다.
i가 소수라면 i의 배수들을 모두 False로 처리합니다.
최종적으로 소수들만 모아서 리스트로 추출합니다.

[입력 예시]
소수를 찾고자 하는 범위의 최댓값 N
'''
import sys
import math

n = int(sys.stdin.readline())

primes = [True] * (n + 1)
primes[0] = False
primes[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if primes[i]:
        j = 2
        while i * j <= n:
            primes[i * j] = False
            j += 1

result = [i for i in range(2, n + 1) if primes[i]]

print(len(result))
for p in result:
    print(p, end=' ')
