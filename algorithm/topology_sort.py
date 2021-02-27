# title: 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 정렬
# src: 이것이 취업을 위한 코딩테스트다 p.296, 297
# time: O(V+E) (V=노드의 개수, E=간선의 개수)

from collections import deque


def topology_sort():
    result = []     # 알고리즘 수행 결과를 담을 리스트
    q = deque()     # 큐

    # 처음 시작할 때 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 -1
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 결과 출력
    for i in result:
        print(i, end=' ')


if __name__ == "__main__":
    v, e = map(int, input().split())    # 노드와 간선의 개수
    indegree = [0] * (v+1)              # 모든 노드에 대한 진입 차수
    graph = [[] for _  in range(v+1)]   # 연결 리스트

    for _ in range(e):
        a, b = map(int, input().split())    # 간선 정보
        graph[a].append(b)
        indegree[b] += 1
        
    topology_sort()