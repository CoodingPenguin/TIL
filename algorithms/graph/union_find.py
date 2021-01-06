# title: 서로소 집합들로 나누어진 노드의 Union과 Find연산
# src: 이것이 취업을 위한 코딩테스트다 p.
# time: 개선 전 - O(VM) / 개선 후 - O(V + MlogV) (V=노드개수, M=연산개수)

def find_parent_basic(parent, x):
    if parent[x] != x:
        return find_parent_basic(parent, parent[x])
    return x

def find_parent_improved(parent, x):
    if parent[x] != x:
        parent[x] = find_parent_improved(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent_improved(parent, a)
    b = find_parent_improved(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":
    v, e = map(int, input().split())
    parent = [0] + list(range(1, v+1))

    # union 연산 
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