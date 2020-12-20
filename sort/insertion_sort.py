# title: 삽입 정렬
# src: 이것이 취업을 위한 코딩테스트다 p.164
# time: O(N^2)

def insertion_sort(arr):
    '''
    삽입 정렬 알고리즘으로 리스트를 정렬
    - `arr`: 1차원 리스트
    '''
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            # 왼쪽으로 이동하면서 자신의 자리를 찾아감
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            # 자기보다 작은 값이 나타나면 거기서 멈춤
            else:
                break

    return arr


if __name__ == "__main__":
    arr = [6, 3, 2, 8, 1, 2, 7, 10]
    print(insertion_sort(arr))