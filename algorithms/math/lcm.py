# title: 최소공배수
# src: https://www.acmicpc.net/problem/2609
# time: O(logN)

def lcm(x, y):
    '''
    math 모듈의 최대공약수를 이용해 최소공배수를 계산한다
    - `x`, `y`: 최소공배수를 구하고자 하는 두 수
    '''
    import math
    return x * y // math.gcd(x, y)


if __name__ == "__main__":
    x, y = 10, 24
    print(lcm(x, y))