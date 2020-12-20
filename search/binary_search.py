# title: 정렬된 리스트에서의 이진 탐색
# src: 이것이 취업을 위한 코딩테스트다 p.189 - p.191
# time: O(logN)

def binary_search_with_recursion(arr, target, start, end):
    '''
    재귀로 구현한 이진탐색 알고리즘
    - `arr`: 정렬된 리스트
    - `target`: 찾으려고 하는 요소
    - `start`, `end`: 탐색의 시작점과 끝점
    '''
    if start > end:
        return None
    mid = (start+end) // 2  # 중간점

    # target을 찾은 경우
    if arr[mid] == target:
        return mid
    # target이 중간점보다 작은 경우
    elif arr[mid] > target:
        return binary_search_with_recursion(arr,  target, start, mid-1)
    # target이 중간점보다 큰 경우
    else:
        return binary_search_with_recursion(arr, target, mid+1, end)


def binary_search_with_loop(arr, target, start, end):
    '''
    반복문로 구현한 이진탐색 알고리즘
    - `arr`: 정렬된 리스트
    - `target`: 찾으려고 하는 요소
    - `start`, `end`: 탐색의 시작점과 끝점
    '''
    while start <= end:
        mid = (start + end) // 2    # 중간점

        # target을 찾은 경우
        if arr[mid] == target:
            return mid
        # target이 중간점보다 작은 경우
        elif arr[mid] > target:
            end = mid - 1
        # target이 중간점보다 큰 경우
        else:
            start = mid + 1
    return None


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    # target이 존재하는 경우
    target = 5
    print("Yes" if binary_search_with_recursion(arr, target, 0, len(arr)-1) else "No")
    print("Yes" if binary_search_with_loop(arr, target, 0, len(arr)-1) else "No")

    # target이 존재하지 않는 경우
    target = 2
    print("Yes" if binary_search_with_recursion(arr, target, 0, len(arr)-1) else "No")
    print("Yes" if binary_search_with_loop(arr, target, 0, len(arr)-1) else "No")