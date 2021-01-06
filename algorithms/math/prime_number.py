# title: 에라토스테네스의 체를 이용한 소수 생성
# src: https://programmers.co.kr/learn/courses/30/lessons/12921
# time: O(N*log(log(N)))

def prime_number(n):
    '''
    에라토스테네스의 체로 n까지의 범위에서의 소수 배열 생성한다
    - `n`: 소수 판정할 1이상의 정수
    '''
    is_prime = [True]*(n+1)
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i in range(2, n+1) if is_prime[i]]


def prime_number_with_set(n):
    '''
    집합을 사용하여 에라토스테네스의 체로 n까지의 범위에서의 소수 배열 생성한다
    - `n`: 소수 판정할 1이상의 정수
    '''
    num = set(range(2, n+1))

    for i in range(2, n+1): 
        if i in num:
            num -= set(range(2*i, n+1, i)) 
    return sorted(num)


if __name__ == "__main__":
    # 입력
    n = 100
    print(prime_number(n))
    print(prime_number_with_set(n))