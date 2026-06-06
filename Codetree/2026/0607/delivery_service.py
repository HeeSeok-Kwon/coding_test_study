import sys
input = sys.stdin.readline


class DeliveryService:
    def __init__(self):
        self.N = 0 # 격자 크기
        self.M = 0 # 택배 개수
        self.grid = [] # 격자
        self.positions = dict() # k, h, w, c
        self.drop_order = [] # 택배 입력된 순서

    def package_input(self, N, M, p_list):
        self.N = N
        self.M = M
        self.grid = [[0 for _ in range(N)] for _ in range(N)]
        
        for p_elem in p_list:
            k = p_elem[0]
            h = p_elem[1]
            w = p_elem[2]
            c = p_elem[3]

            self.positions[k] = {"k": k, "h": h, "w": w, "c": c - 1, "r": None, "placed": None}
            self.drop_order.append(k)

        for k in self.drop_order:
            h = self.positions[k]["h"]
            w = self.positions[k]["w"]
            c = self.positions[k]["c"]

            # 0행에 올 수 있는지 검사
            if not self.package_can_place(0, h, w, c):
                self.positions[k]["r"] = None
                self.positions[k]["placed"] = False
                continue

            r = 0

            while self.package_can_place(r + 1, h, w, c):
                r += 1

            self.positions[k]["r"] = r
            self.positions[k]["placed"] = True

            for row in range(r, r + h):
                for col in range(c, c + w):
                    self.grid[row][col] = k

        # print(self.grid)

    def package_can_place(self, r, h, w, c):

        if(r + h > self.N):
            return False
        if(c + w > self.N):
            return False
        
        for row in range(r, r + h):
            for col in range(c, c + w):
                if(self.grid[row][col] != 0):
                    return False
        
        return True
    
    def package_drop_off_left(self, r, h, w, c):
        for row in range(r, r + h):
            for col in range(0, c):
                if(self.grid[row][col] != 0):
                    return False
                
        return True
    
    def package_drop_off_right(self, r, h, w, c):
        for row in range(r, r + h):
            for col in range(c + w, self.N):
                if(self.grid[row][col] != 0):
                    return False
                
        return True
    
    def package_drop_off(self, direction):
        
        candidates = []

        if(direction == "left"):
            for k, info in self.positions.items():
                if(not info["placed"]):
                    continue
                
                r = info["r"]
                h = info["h"]
                w = info["w"]
                c = info["c"]

                result = self.package_drop_off_left(r, h, w, c)

                if(result):
                    candidates.append(k)

            if not candidates:
                return None

            target = min(candidates)

            target_position = self.positions[target]
            target_r = target_position["r"]
            target_h = target_position["h"]
            target_c = target_position["c"]
            target_w = target_position["w"]

            for row in range(target_r, target_r + target_h):
                for col in range(target_c, target_c + target_w):
                    self.grid[row][col] = 0

            self.positions[target]["placed"] = False
            return target

        elif(direction == "right"):
            for k, info in self.positions.items():
                if(not info["placed"]):
                    continue
                
                r = info["r"]
                h = info["h"]
                w = info["w"]
                c = info["c"]

                result = self.package_drop_off_right(r, h, w, c)

                if(result):
                    candidates.append(k)

            if not candidates:
                return None

            target = min(candidates)

            target_position = self.positions[target]
            target_r = target_position["r"]
            target_h = target_position["h"]
            target_c = target_position["c"]
            target_w = target_position["w"]

            for row in range(target_r, target_r + target_h):
                for col in range(target_c, target_c + target_w):
                    self.grid[row][col] = 0

            self.positions[target]["placed"] = False
            return target

        elif(direction == "down"):
            self.grid = [[0 for _ in range(self.N)] for _ in range(self.N)]

            for k, info in self.positions.items():
                placed = info["placed"]

                if(not placed): 
                    continue 
                
                h = info["h"]
                w = info["w"]
                c = info["c"]

                # 0행에 올 수 있는지 검사
                if not self.package_can_place(0, h, w, c):
                    self.positions[k]["r"] = None
                    self.positions[k]["placed"] = False
                    continue

                r = 0

                while self.package_can_place(r + 1, h, w, c):
                    r += 1

                self.positions[k]["r"] = r
                self.positions[k]["placed"] = True

                for row in range(r, r + h):
                    for col in range(c, c + w):
                        self.grid[row][col] = k



def solve():
    deliveryService = DeliveryService()

    N, M = map(int, input().split())
    p_list = []

    for _ in range(M):
        k, h, w, c = map(int, input().split())
        p_list.append([k, h, w, c])

    deliveryService.package_input(N, M, p_list)

    result = [] # 결과를 담을 변수

    while len(result) < M:
        k = deliveryService.package_drop_off("left")

        if k is not None:
            result.append(k)

        deliveryService.package_drop_off("down")

        if len(result) == M:
            break

        k = deliveryService.package_drop_off("right")

        if(k is not None):
            result.append(k)

        deliveryService.package_drop_off("down")

    print(*result, sep='\n')

    

if __name__ == "__main__":
    solve()