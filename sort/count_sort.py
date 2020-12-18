# title: 계수 정렬

def count_sort(arr):
    '''
    계수 정렬 알고리즘으로 리스트를 정렬
    - arr: 모든 요소가 음이 아닌 정수로 이루어진 1차원 리스트
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


if __name__ == "__main__":
    arr = [0, 0, 2, 1, 5, 2, 4, 9, 2, 2, 4, 2, 3]
    print(count_sort(arr))