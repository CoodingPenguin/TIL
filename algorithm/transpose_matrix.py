# title: 2차원 리스트 슬라이싱
# src: https://velog.io/@tjdud0123/프렌즈-4블록-2018-카카오-공채-python


def transpose_matrix(matrix):
    '''
    행렬을 전치시킨다
     - `matrix`: n*m으로 이루어진 행렬 (n과 m은 양의 정수)
    '''
    return list(zip(*matrix))

if __name__ == '__main__':
    matrix = [[1, 2, 3, 4, 5],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 2, 2]]
    matrix_t = transpose_matrix(matrix)
    for row in matrix_t:
        print(row)