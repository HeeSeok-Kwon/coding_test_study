import sys
from collections import deque
input = sys.stdin.readline


class AiRobot:
    def __init__(self):
        self.N = 0 # 격자의 크기
        self.K = 0 # 로봇청소기 갯수
        self.L = 0 # 테스트 횟수

        self.grid = [] # 격자
        self.positions = deque() # 로봇청소기 위치

    def init(self, N, K, L, grid, positions):
        self.N = N
        self.K = K
        self.L = L

        self.grid = grid
        self.positions = positions

        self.DIRECTION = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우

        self.ROBOT_FACING = [
            [(-1, 0), (0, 0), (1, 0), (0, 1)], # 오른쪽
            [(0, -1), (0, 0), (0, 1), (1, 0)], # 아래쪽
            [(-1, 0), (0, 0), (1, 0), (0, -1)], # 왼쪽
            [(0, -1), (0, 0), (0, 1), (-1, 0)] # 위쪽
        ]

    def move(self):
        new_positions = deque()
        robot_set = set(map(tuple, self.positions))

        while self.positions:
            r_x, r_y = self.positions.popleft() 
            visited = [[False] * self.N for _ in range(self.N)]
            
            robot_set.remove((r_x, r_y))            
            visited[r_x][r_y] = True

            q = deque()
            q.append((0, r_x, r_y))
            candidates = []

            while q:
                dist, x, y = q.popleft()

                if self.grid[x][y] > 0:
                    candidates.append((dist, x, y))
                    continue

                for (dx, dy) in self.DIRECTION:
                    nx = x + dx
                    ny = y + dy

                    if nx < 0 or nx >= self.N or ny < 0 or ny >= self.N:
                        continue
                    if visited[nx][ny]:
                        continue
                    if self.grid[nx][ny] == -1:
                        continue
                    if (nx, ny) in robot_set:
                        continue

                    visited[nx][ny] = True
                    q.append((dist + 1, nx, ny))

            candidates.sort()

            if(len(candidates) > 0):
                _, next_x, next_y = candidates[0]
            else:
                next_x, next_y = r_x, r_y

            robot_set.add((next_x, next_y))
            new_positions.append([next_x, next_y])

        self.positions = new_positions

    def clean(self):

        for (x, y) in self.positions:
            max_sum = 0
            max_sum_idx = 0

            for idx, facing_direction in enumerate(self.ROBOT_FACING):
                clean_sum = 0
                for (dx, dy) in facing_direction:
                    nx, ny = x + dx, y + dy

                    if nx < 0 or nx >= self.N or ny < 0 or ny >= self.N:
                        continue
                    else:
                        if self.grid[nx][ny] > 0:
                            clean_sum += min(self.grid[nx][ny], 20)

                if(clean_sum > max_sum):
                    max_sum = clean_sum
                    max_sum_idx = idx

            for (clean_x, clean_y) in self.ROBOT_FACING[max_sum_idx]:
                nx, ny = x + clean_x, y + clean_y
                if nx < 0 or nx >= self.N or ny < 0 or ny >= self.N:
                    continue
                else:
                    if self.grid[nx][ny] > 0:
                        self.grid[nx][ny] = max(0, self.grid[nx][ny] - 20)
            

    def accumulate(self):
        for i in range(self.N):
            for j in range(self.N):
                if(self.grid[i][j] > 0):
                    self.grid[i][j] += 5
    
    def spread(self):
        new_grid = []
        
        for i in range(self.N):
            new_grid_row = []
            for j in range(self.N):
                if(self.grid[i][j] == -1):
                    new_grid_row.append(self.grid[i][j])
                elif(self.grid[i][j] > 0):
                    new_grid_row.append(self.grid[i][j])
                else:
                    up, down, left, right = 0, 0, 0, 0

                    if(i-1 > -1):
                        up = self.grid[i-1][j] if self.grid[i-1][j] > 0 else 0
                    if(i+1 < self.N):
                        down = self.grid[i+1][j] if self.grid[i+1][j] > 0 else 0
                    if(j-1 > -1):
                        left = self.grid[i][j-1] if self.grid[i][j-1] > 0 else 0
                    if(j+1 < self.N):
                        right = self.grid[i][j+1] if self.grid[i][j+1] > 0 else 0

                    new_grid_row.append((up + down + left + right) // 10)

            new_grid.append(new_grid_row)
        
        self.grid = new_grid

    def get_dust_sum(self):
        dust_sum = 0
        
        for i in range(self.N):
            for j in range(self.N):
                if(self.grid[i][j] > -1):
                    dust_sum += self.grid[i][j]

        return dust_sum




def solve():
    aiRobot = AiRobot()

    # 입력부
    N, K, L = map(int, input().split())
    grid = []
    positions = deque()

    for _ in range(N):
        row = list(map(int, input().split()))
        grid.append(row)
    
    for _ in range(K):
        x, y = list(map(int, input().split()))
        positions.append([x-1, y-1])

    # 초기화
    aiRobot.init(N=N, K=K, L=L, grid=grid, positions=positions)

    # 실행부
    for _ in range(L):
        # 초기 청소기 위치
        # print(aiRobot.positions)
        
        # 청소기 이동
        aiRobot.move()
        # 이동 후 청소기 위치
        # print(aiRobot.positions)
        
        # 청소
        aiRobot.clean()
        # 먼지 축적
        aiRobot.accumulate()
        # 먼지 확산
        aiRobot.spread()
        # print(aiRobot.grid)

        # 먼지 합
        result = aiRobot.get_dust_sum()
        print(result)
        


if __name__ == "__main__":
    solve()