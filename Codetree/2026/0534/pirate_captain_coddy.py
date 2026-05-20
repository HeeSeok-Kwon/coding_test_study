import sys
import heapq
input = sys.stdin.readline


class PirateCaptainCoddy:
    def __init__(self):
        self.N = 0 # 초기 선박 개수
        self.ships = [] # 선박 정보 담을 리스트

    def ready_to_attack(self, N, ships):
        self.N = N
        self.ships = ships
        pass

    def request_support(self): # 파라미터 필요
        pass

    def gun_replacement(self): # 파라미터 필요
        pass

    def attack(self):
        pass
    

def solve():
    pirateCaptainCoddy = PirateCaptainCoddy()

    T = int(input().strip())

    for _ in range(T):
        cmd = list(map(int, input().split()))
        order = cmd[0]

        if(order == 100):
            pirateCaptainCoddy.ready_to_attack(N=0, ships=[])
        elif(order == 200):
            pirateCaptainCoddy.request_support()
        elif(order == 300):
            pirateCaptainCoddy.gun_replacement()
        elif(order == 400):
            pirateCaptainCoddy.attack()
    


if __name__ == "__main__":
    solve()