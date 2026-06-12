import sys
input = sys.stdin.readline


class QueenAnt:
    def __init__(self):
        self.ant_house = [] # x 좌표
        self.removed = []

    def village_construction(self, N, ant_house):
        self.ant_house = [0] + ant_house
        self.removed = [False] * (N + 1)

    def ant_house_building(self, p):
        x = p # x 좌표
        self.ant_house.append(x)
        self.removed.append(False)
        
    def ant_house_removal(self, q):
        self.removed[q] = True

    def ant_house_patrol(self, r):
        left = 0
        right = 10**9

        while left < right:
            mid = (left + right) // 2

            # 필요한 개미 수 구하기
            ant_cnt = self.get_ant_count(mid)

            if(ant_cnt <= r):
                right = mid
            else:
                left = mid + 1
        
        return left

    def get_ant_count(self, mid):
        ant_cnt = 0
        start_x = None

        for i in range(1, len(self.ant_house)):
            if(self.removed[i]):
                continue

            if(start_x is None):
                ant_cnt += 1
                start_x = self.ant_house[i]
            else:
                current_x = self.ant_house[i]

                if(current_x - start_x <= mid):
                    continue
                else:
                    ant_cnt += 1
                    start_x = current_x

        return ant_cnt


def solve():
    queenAnt = QueenAnt()

    Q = int(input())

    result = []

    for _ in range(Q):
        cmd = list(map(int, input().split()))
        order = cmd[0]

        if(order == 100):
            N = cmd[1]
            ant_house = cmd[2:]

            queenAnt.village_construction(N, ant_house)

        elif(order == 200):
            p = cmd[1]

            queenAnt.ant_house_building(p)

        elif(order == 300):
            q = cmd[1]

            queenAnt.ant_house_removal(q)

        elif(order == 400):
            r = cmd[1]

            t = queenAnt.ant_house_patrol(r)

            result.append(t)

    print(*result, sep="\n")



if __name__ == "__main__":
    solve()