# title: 너비 우선 탐색(BFS, Breadth First Search)
# src: 이것이 취업을 위한 코딩테스트다 p.147
# time: O(V) 

from collections import deque


def bfs(graph, start, visited):
    '''
    너비를 우선으로 하여 전 노드를 탐색
    - `graph`: 노드 연결 정보 (2차원 리스트)
    - `start`: 시작 노드
    - `visited`: 노드 방문 정보 (1차원 리스트)
    '''
    # 방문하지 않은 인접 노드 저장
    # 처음은 시작 노드로 시작
    queue = deque([start])

    # 현재 노드 방문 처리
    visited[start] = True

    # 큐가 비워질 때 까지
    # 즉, 더이상의 방문하지 않은 인접노드가 없을 때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        
        # 현재 노드의 인접 노드 탐색
        for i in graph[v]:
            # 방문하지 않았다면 큐에 추가하고 방문 표시
            if not visited[i]:
                queue.append(i)
                visited[i] = True


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

    bfs(graph, 1, visited)