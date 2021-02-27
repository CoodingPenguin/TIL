# title: 시계방향으로 행렬을 90도 회전
# src: 이것이 취업을 위한 코딩테스트다 p. 520
# src: https://github.com/tjdud0123/daily_algorithm#-90도-회전

def rotate_90_with_loop(matrix):
    '''
    행렬을 90도 회전한다
    - `matrix`: n*m으로 이루어진 행렬 (n과 m은 양의 정수)
    '''
    row = len(matrix)       # 행의 길이
    col = len(matrix[0])    # 열의 길이 

    result = [[0]*row for _ in range(col)]
    for i in range(row):
        for j in range(col):
            result[j][row-i-1] = matrix[i][j]
    
    return result

def rotate_90_with_zip(matrix):
    '''
    행렬을 90도로 회전한다
     - `matrix`: n*m으로 이루어진 행렬 (n과 m은 양의 정수)
    '''
    # 1. 행렬의 행을 뒤집는다. 
    # 2. 각 행의 요소를 가져와 하나의 행으로 만든다.
    return list(zip(*matrix[::-1]))

if __name__ == '__main__':
    before = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    after1 = rotate_90_with_loop(before)
    after2 = rotate_90_with_zip(before)

    for i in range(len(before)):
        print(after1[i])
    print()
    for i in range(len(before)):
        print(after2[i])