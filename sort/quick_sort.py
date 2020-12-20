# title: 퀵 정렬
# src: 이것이 취업을 위한 코딩테스트다 p.169
# time: O(NlogN)

def quick_sort(arr):
    '''
    퀵 정렬 알고리즘으로 리스트를 정렬
    - `arr`: 1차원 리스트
    '''
    # 리스트의 요소의 개수가 하나 이하면 정렬할 필요가 없으므로 종료
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # 첫 번째 요소가 피벗
    tail = arr[1:]  # 피벗을 제외한 리스트 요소

    left_side = [x for x in tail if x <= pivot] # 피벗 기준으로 왼쪽 리스트
    right_side = [x for x in tail if x > pivot] # 피벗 기준으로 오른쪽 리스트

    # 피벗을 기준으로 분할된 왼쪽, 오른쪽 리스트를 정렬한 뒤 병합
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


if __name__ == "__main__":
    arr = [6, 3, 2, 8, 1, 2, 7, 10]
    print(quick_sort(arr))