# title: 최대공약수
# src: https://www.acmicpc.net/problem/2609
# time: O(logN)

def gcd_with_euclidean(x, y):
    '''
    유클리드 호제법으로 최대공약수 계산한다
    - `x`, `y`: 최대공약수를 구하고자 하는 두 수
    '''
    if y == 0:
        return x
    return gcd_with_euclidean(y, x%y)


def gcd_with_math_module(x, y):
    '''
    math.gcd()로 최대공약수 계산한다
    - `x`, `y`: 최대공약수를 구하고자 하는 두 수   
    '''
    import math
    return math.gcd(x, y)


if __name__ == "__main__":
    x, y = 10, 24
    print(gcd_with_euclidean(x, y))
    print(gcd_with_math_module(x, y))