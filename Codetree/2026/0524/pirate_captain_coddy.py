import sys
import heapq
input = sys.stdin.readline


class PirateCaptainCoddy:
    def __init__(self):
        self.N = 0 # 초기 선박 개수
        self.ships = dict() # 선박 정보 담을 딕셔너리
        self.attack_list = []
        self.timer = 0

    def ready_to_attack(self, N, ship_infos):
        self.N = N
        self.ships = dict()
        self.attack_list = []
        self.timer = 0

        for i in range(N):
            ship_id = ship_infos[i*3]
            ship_power = ship_infos[i*3 + 1]
            ship_reload = ship_infos[i*3 + 2]

            self.ships[ship_id] = {"id": ship_id, "power": ship_power, "reload": ship_reload, "last": -ship_reload}

            heapq.heappush(self.attack_list, (-ship_power, ship_id))
        
        # print(f"N: {N}")
        # print(f"ships: {ships}")

    def request_support(self, id, power, reload):
        self.ships[id] = {"id": id, "power": power, "reload": reload, "last": -reload}
        heapq.heappush(self.attack_list, (-power, id))

    def gun_replacement(self, id, power):
        self.ships[id]["power"] = power
        heapq.heappush(self.attack_list, (-power, id))

    def attack(self):

        new_attack_list = []
        total_attack = 0
        total_ship_cnt = 0
        total_ships = []

        while self.attack_list and total_ship_cnt < 5:
            power, id = heapq.heappop(self.attack_list)

            power = -power # 음수를 양수로 부호변환
            origin_power = self.ships[id]["power"]

            if(origin_power != power):
                continue

            origin_reload = self.ships[id]["reload"]
            origin_last = self.ships[id]["last"]

            if(self.timer >= origin_reload + origin_last):
                total_attack += power
                total_ship_cnt += 1
                total_ships.append(id)

                self.ships[id]["last"] = self.timer
            
            heapq.heappush(new_attack_list, (-power, id))

        print(total_attack, total_ship_cnt, *total_ships)

        for item in new_attack_list:
            heapq.heappush(self.attack_list, item)
    

def solve():
    pirateCaptainCoddy = PirateCaptainCoddy()

    T = int(input().strip())

    for _ in range(T):
        cmd = list(map(int, input().split()))
        order = cmd[0]

        if(order == 100):
            N = cmd[1]
            ship_infos = cmd[2:]
            pirateCaptainCoddy.ready_to_attack(N=N, ship_infos=ship_infos)

        elif(order == 200):
            ship_id = cmd[1]
            ship_power = cmd[2]
            ship_reload = cmd[3]

            pirateCaptainCoddy.request_support(ship_id, ship_power, ship_reload)

        elif(order == 300):
            ship_id = cmd[1]
            ship_power = cmd[2]

            pirateCaptainCoddy.gun_replacement(ship_id, ship_power)

        elif(order == 400):
            pirateCaptainCoddy.attack()

        pirateCaptainCoddy.timer += 1 # 시간 증가
    


if __name__ == "__main__":
    solve()