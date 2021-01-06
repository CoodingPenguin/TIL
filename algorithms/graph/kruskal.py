# title: 최소 신장 트리 알고리즘 중 하나인 크루스칼 알고리즘
# src: 이것이 취업을 위한 코딩테스트다 p.288, 289
# time: O(ElogE) (E=간선의 개수)

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
    edges = []      # 모든 간선을 담을 리스트
    result = 0      # 최종 비용                    

    for _ in range(e):
        a, b, cost = map(int, input().split())
        # 비용순으로 정렬하기 위해 비용을 가장 앞으로 설정
        edges.append((cost, a, b))

    # 간선을 비용순으로 정렬
    edges.sort()

    for edge in edges:
        cost, a, b = edge
        # 간선을 확인하며 사이클이 발생하지 않는 경우만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    
    print(result)