class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]


        # DFS 탐색 가능한 그래프 만들기
        for i in range(0, len(prerequisites)):
            take_after = prerequisites[i][0]
            take_first = prerequisites[i][1]

            graph[take_first].append(take_after)

        # 탐색 시작
        def dfs(graph, v, visited):
            # 1. 현재 노드를 탐색 중 처리
            visited[v] = 1

            # 2. 현재 노드와 연결된 다른 노드를 재귀적으로 방문
            for i in graph[v]:
                if visited[i] == 0:
                    if dfs(graph, i, visited) == False:
                        return False
                elif visited[i] == 1:
                    return False

            visited[v] = 2
            return True

        visited = [0] * numCourses # 0: 방문 안 함, 1: 탐색 중, 2: 탐색 완료

        for i in range(numCourses):
            if visited[i] == 0:
                if dfs(graph, i, visited) == False:
                    return False

        return True

        