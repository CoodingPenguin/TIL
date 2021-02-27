# title: 서로소 집합 알고리즘으로 그래프 사이클 판별
# src: 이것이 취업을 위한 코딩테스트다 p.279, 280
# time: 개선 전 - O(VM) / 개선 후 - O(V + MlogV) (V=노드개수, M=연산개수)


def find_parent(parent, x):
    '''
    재귀적으로 특정 원소가 속한 집합을 찾아 부모 테이블을 갱신한다
    - `parent`: 1차원 부모 테이블
    - `x`: 부모를 찾으려는 노드 번호
    '''
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    '''
    두 원소가 속한 집합을 합친다
    - `parent`: 1차원 부모 테이블
    - `a`, `b`: 합치려는 노드 번호
    '''
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":
    v, e = map(int, input().split())    # 노드와 간선의 개수
    parent = [0] + list(range(1, v+1))  # 부모 테이블
    cycle = False                       # 사이클 발생 여부

    for i in range(e):
        a, b = map(int, input().split())
        # 사이클이 발생한 경우 종료
        if find_parent(parent, a) == find_parent(parent, b):
            cycle = True
            break
        # 사이클이 발생하지 않았따면 Union 연산 수행
        else:
            union_parent(parent, a, b)

    if cycle:
        print('사이클이 발생했습니다.')
    else:
        print('사이클이 발생하지 않았습니다.')