# title: 정렬된 리스트에서 특정 범위에 속하는 원소의 개수 계산
# src: 이것이 취업을 위한 코딩테스트다 p.457
# time: O(logN)

from bisect import bisect_left, bisect_right


def count_by_range(arr, left_value, right_value):
    '''
    정렬된 리스트에서 특정 범위에 속하는 요소의 개수 계산
    - `arr`: 정수로 이루어진 정렬된 리스트
    - `left_value`, `right_value`: left_value ~ right_value의 범위
    '''
    right_idx = bisect_right(arr, right_value)
    left_idx = bisect_left(arr, left_value)
    return right_idx - left_idx


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 7, 8, 8, 8]
    print(count_by_range(arr, 6, 6))
    print(count_by_range(arr, 2, 7))