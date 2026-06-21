import sys
input = sys.stdin.readline
from collections import deque

class MicrobialResearch:
    def __init__(self):
        self.N = 0 # 격자 크기
        self.Q = 0
        self.grid = [] # 격자
        self.next_q_num = 0 # 각 미생물 고유번호

    def microbial_set(self, N, Q):
        self.N = N
        self.Q = Q

        self.grid = [[0] * N for _ in range(N)]

    def microbial_input(self, microbial):

        r1, c1, r2, c2 = microbial

        self.next_q_num += 1

        for x in range(r1, r2):
            for y in range(c1, c2):
                self.grid[x][y] = self.next_q_num

        # 나눠진 부분이 있는지 검사
        visited = [[False] * self.N for _ in range(self.N)]

        q_num_count = {} # 각 미생물 번호별 덩어리 개수

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for x in range(self.N):
            for y in range(self.N):

                if self.grid[x][y] == 0:
                    continue

                if visited[x][y]:
                    continue

                q_num = self.grid[x][y]

                if q_num not in q_num_count:
                    q_num_count[q_num] = 0

                q_num_count[q_num] += 1

                queue = deque([(x, y)])
    
                # 현재 노드를 방문 처리
                visited[x][y] = True
                
                while queue:
                    c_x, c_y = queue.popleft()
                    
                    for i in range(4):
                        nx = c_x + dx[i]
                        ny = c_y + dy[i]

                        if(nx < 0 or nx >= self.N or ny < 0 or ny >= self.N):
                            continue

                        if visited[nx][ny]:
                            continue

                        if self.grid[nx][ny] != q_num:
                            continue

                        visited[nx][ny] = True
                        queue.append((nx, ny))

        remove_microbe = set()

        for q_num in q_num_count:
            if(q_num_count[q_num] >= 2):
                remove_microbe.add(q_num)

        for x in range(self.N):
            for y in range(self.N):
                if self.grid[x][y] in remove_microbe:
                    self.grid[x][y] = 0

    def microbial_transferring(self):
        pass

    def microbial_result(self):
        pass

                

def solve():
    microbialResearch = MicrobialResearch()

    N, Q = map(int, input().split())

    microbialResearch.microbial_set(N, Q)

    for _ in range(Q):
        r1, c1, r2, c2 = map(int, input().split())
        
        microbialResearch.microbial_input([r1, c1, r2, c2])

        microbialResearch.microbial_transferring()

        microbialResearch.microbial_result()


if __name__ == "__main__":
    solve()
