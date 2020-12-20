# title: 깊이 우선 탐색(DFS, Depth First Search)
# src: 이것이 취업을 위한 코딩테스트다 p.142

def dfs(graph, v, visited):
    '''
    깊이를 우선으로 하여 전 노드를 탐색
    - `graph`: 노드 연결 정보 (2차원 리스트)
    - `v`: 시작 노드
    - `visited`: 노드 방문 정보 (1차원 리스트)
    '''
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=" ")

    # 현재 노드와 연결된 다른 노드 중
    # 방문하지 않은 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


if __name__=='__main__':
    graph = [
        [], # 인덱스와 숫자를 맞추기 위한 빈 리스트
        [5],
        [4, 6],
        [5],
        [2, 6],
        [3, 6],
        [2, 4, 5],
    ]
    visited = [False] * len(graph)

    dfs(graph, 1, visited)