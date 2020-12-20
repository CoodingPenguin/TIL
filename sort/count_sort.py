# title: 계수 정렬
# O(N+K) (N=데이터개수, K=최대값)

def count_sort(arr):
    '''
    계수 정렬 알고리즘으로 리스트를 정렬
    - `arr`: 모든 요소가 음이 아닌 정수로 이루어진 1차원 리스트
    '''
    # 각 요소별 개수 세기
    count = [0] * (max(arr)+1)
    for num in arr:
        count[num] += 1
    
    # 요소의 개수만큼 요소 생성
    result = []
    for idx, value in enumerate(count):
        if value:
            result.extend([idx]*value)
    
    return result


def count_sort_with_counter(arr):
    '''
    Counter를 사용하여 구현한 계수 정렬 알고리즘
    - arr: 모든 요소가 음이 아닌 정수로 이루어진 1차원 리스트
    '''
    from collections import Counter
    
    # 각 요소별 개수 세기
    counter = Counter()
    for num in arr:
        counter[num] += 1
    
    # 요소의 개수만큼 요소 생성
    result = []
    for key, value in sorted(counter.items()):
        result.extend([key]*value)
    
    return result


if __name__ == "__main__":
    arr = [0, 0, 2, 1, 5, 2, 4, 9, 2, 2, 4, 2, 3]
    print(count_sort(arr))
    print(count_sort_with_counter(arr))