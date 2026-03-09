'''
유클리드 호제법 (Euclidean Algorithm)
두 수의 최대공약수(GCD)를 O(log N)의 매우 빠른 속도로 구하는 알고리즘.
최소공배수(LCM)는 두 수의 곱을 최대공약수로 나누어 쉽게 구할 수 있습니다.

[입력 예시]
두 정수 A와 B
'''
import sys

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b, g):
    return (a * b) // g

a, b = map(int, sys.stdin.readline().split())

g = gcd(a, b)
l = lcm(a, b, g)

print(g)
print(l)
