# title: 시계방향으로 행렬을 90도 회전
# src: 이것이 취업을 위한 코딩테스트다 p. 520

def rotate_a_matrix_by_90_degree(matrix):
    '''
    행렬을 90도 회전
    - `matrix`: n*m으로 이루어진 행렬 (n과 m은 양의 정수)
    '''
    row = len(matrix)       # 행의 길이
    col = len(matrix[0])    # 열의 길이 

    result = [[0]*row for _ in range(col)]
    for i in range(row):
        for j in range(col):
            result[j][row-i-1] = matrix[i][j]
    
    return result


if __name__ == '__main__':
    before = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    after = rotate_a_matrix_by_90_degree(before)

    for i in range(len(before)):
        print(after[i])