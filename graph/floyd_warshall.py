# title: 플로이드-워셜 최단 경로 알고리즘
# src: 이것이 취업을 위한 코딩테스트다 p.257 - p.258
# time: O(N^2)

INF = int(1e9)  # 무한

def floyd_warshall(graph):
    '''
    모든 지점에서 다른 모든 지점까지의 최단 경로를 구하는 동적계획법 알고리즘
    - `graph`: 2차원 인접 행렬
    '''
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                # a-b와 a-k-b 중 가장 비용이 적은 걸로 갱신
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])


if __name__ == "__main__":
    n, m = int(input()), int(input())   # 노드와 간선의 개수
    graph = [[INF]*(n+1) for _ in range(n+1)]   # 인접 행렬

    # 자기 자신 - 자기 자신은 0으로 초기화
    for a in range(1, n+1):
        graph[a][a] = 0
    
    # 각 간선에 대한 정보 입력
    for _ in range(m):
        a, b, c = map(int, input().split())
        # a에서 b까지 가는 데 쓰는 비용 c
        graph[a][b] = c
    
    floyd_warshall(graph)

    for row in graph[1:]:
        print(' '.join(map(str, row[1:])))