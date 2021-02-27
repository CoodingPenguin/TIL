# title: 서로소 집합들로 나누어진 노드의 Union과 Find연산
# src: 이것이 취업을 위한 코딩테스트다 p.273 - 276
# time: 개선 전 - O(VM) / 개선 후 - O(V + MlogV) (V=노드개수, M=연산개수)

def find_parent_basic(parent, x):
    '''
    재귀적으로 특정 원소가 속한 집합을 찾는다
    - `parent`: 1차원 부모 테이블
    - `x`: 부모를 찾으려는 노드 번호
    '''
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent_basic(parent, parent[x])
    return x


def find_parent_improved(parent, x):
    '''
    재귀적으로 특정 원소가 속한 집합을 찾아 부모 테이블을 갱신한다
    - `parent`: 1차원 부모 테이블
    - `x`: 부모를 찾으려는 노드 번호
    '''
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent_improved(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    '''
    두 원소가 속한 집합을 합친다
    - `parent`: 1차원 부모 테이블
    - `a`, `b`: 합치려는 노드 번호
    '''
    a = find_parent_improved(parent, a)
    b = find_parent_improved(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":
    v, e = map(int, input().split())    # 노드와 간선의 개수
    parent = [0] + list(range(1, v+1))  # 부모 테이블

    # 입력 받은 노드 값에 대한 Union 연산 실행
    for i in range(e):
        a, b = map(int, input().split())
        union_parent(parent, a, b)
    
    # 각 원소가 속한 집합 출력
    print('각 원소가 속한 집합: ', end='')
    for i in range(1, v+1):
        print(find_parent_improved(parent, i), end=' ')
    print()

    # 부모 테이블 출력
    print('부모 테이블 :', end='')
    for i in range(1, v+1):
        print(parent[i], end=' ')