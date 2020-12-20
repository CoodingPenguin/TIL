# title: 선택 정렬
# src: 이것이 취업을 위한 코딩테스트다 p.159
# time: O(N) ~ O(N^2)

def selection_sort(arr):
    '''
    선택 정렬 알고리즘으로 리스트를 정렬
    - `arr`: 1차원 리스트
    '''
    for i in range(len(arr)):
        min_idx = i     # 가장 작은 원소의 인덱스 값
        for j in range(i+1, len(arr)):
            # min_idx의 값보다 더 작은 값이 나타나면 인덱스 갱신
            if arr[min_idx] > arr[j]:
                min_idx = j
        # 현재 인덱스에 있는 값과 가장 작은 수와 swap
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


if __name__ == "__main__":
    arr = [6, 3, 2, 8, 1, 2, 7, 10]
    print(selection_sort(arr))