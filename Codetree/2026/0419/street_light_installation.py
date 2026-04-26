import sys
import heapq
input = sys.stdin.readline


class StreetLightInstallation:
    def __init__(self):
        self.N = 0 # 전체 거리 크기
        self.M = 0 # 초기 가로등 개수

        # id -> position
        self.pos = [0]

        # id -> left/right neighbor id
        self.prev = [0]
        self.next = [0]

        # 삭제 여부
        self.removed = [False]

        # (-gap, left_pos, left_id, right_id)
        self.gap_heap = []

        # 가장 왼쪽/오른쪽 가로등 관리용
        self.left_heap = []
        self.right_heap = []

        # 새 가로등 id 발급용
        self.next_id = 1

    def init(self, N, M, positions):
        self.N = N
        self.M = M

        self.pos = [0] + positions
        self.prev = [0] * (M + 1)
        self.next = [0] * (M + 1)
        self.removed = [False] * (M + 1)

        self.gap_heap = []
        self.left_heap = []
        self.right_heap = []

        self.next_id = M + 1

        # 1. 양방향 연결 리스트 구성
        for i in range(1, M + 1):
            self.prev[i] = i - 1 if i > 1 else 0
            self.next[i] = i + 1 if i < M else 0

        # 2. 구간 힙 초기화
        for i in range(1, M):
            self.push_gap(i, i + 1)

        # 3. 양끝 힙 초기화
        for i in range(1, M + 1):
            heapq.heappush(self.left_heap, (self.pos[i], i))
            heapq.heappush(self.right_heap, (-self.pos[i], i))

    def push_gap(self, left_id, right_id):
        # left_id, right_id가 0이면 구간 없음
        if left_id == 0 or right_id == 0:
            return

        gap = self.pos[right_id] - self.pos[left_id]
        heapq.heappush(
            self.gap_heap,
            (-gap, self.pos[left_id], left_id, right_id)
        )

    def is_valid_gap(self, left_id, right_id):
        if self.removed[left_id] or self.removed[right_id]:
            return False

        if self.next[left_id] != right_id:
            return False
        if self.prev[right_id] != left_id:
            return False

        return True

    def clean_gap_heap(self):
        while self.gap_heap:
            gap, left_pos, left_id, right_id = self.gap_heap[0]

            if self.is_valid_gap(left_id, right_id):
                return self.gap_heap[0]

            heapq.heappop(self.gap_heap)

        return None

    def clean_left_heap(self):
        while self.left_heap:
            pos, left_id = self.left_heap[0]

            if self.removed[left_id]:
                heapq.heappop(self.left_heap)
            else:
                return self.left_heap[0]

        return None

    
    def clean_right_heap(self):
        while self.right_heap:
            pos, right_id= self.right_heap[0]

            if self.removed[right_id]:
                heapq.heappop(self.right_heap)
            else:
                return self.right_heap[0]

        return None

    def add_light(self):
        # 1. clean_gap_heap()으로 가장 긴 유효 구간 찾기
        gap_info = self.clean_gap_heap()

        if gap_info is None:
            return

        gap, left_pos, left_id, right_id = gap_info

        right_pos = self.pos[right_id]

        new_pos = (left_pos + right_pos + 1) // 2
        
        # 3. 새 id 생성
        new_id = self.next_id
        self.next_id += 1

        # 4. pos/prev/next/removed 배열 확장
        self.pos.append(new_pos)
        self.prev.append(left_id)
        self.next.append(right_id)
        self.removed.append(False)

        # 5. left -> new -> right 연결 갱신
        self.prev[right_id] = new_id
        self.next[left_id] = new_id

        # 6. 새 구간 2개 push
        self.push_gap(left_id, new_id)
        self.push_gap(new_id, right_id)

        # 7. left_heap/right_heap에도 새 가로등 push
        heapq.heappush(self.left_heap, (new_pos, new_id))
        heapq.heappush(self.right_heap, (-new_pos, new_id))


    def remove_light(self, x):
        if self.removed[x]:
            return
        
        left = self.prev[x]
        right = self.next[x]
        
        self.removed[x] = True

        if left != 0:
            self.next[left] = right

        if right != 0:
            self.prev[right] = left

        if left != 0 and right != 0:
            self.push_gap(left, right)


    def query_power(self):
        # 1. 가장 왼쪽 살아있는 가로등 찾기
        left_info = self.clean_left_heap()
        left_pos, _ = left_info

        left_candidate = (left_pos - 1) * 2

        # 2. 가장 오른쪽 살아있는 가로등 찾기
        right_info = self.clean_right_heap()
        right_pos, _ = right_info

        right_pos = -right_pos

        right_candidate = (self.N - right_pos) * 2

        # 3. 가장 긴 유효 내부 구간 찾기
        gap_info = self.clean_gap_heap()

        if gap_info is None:
            inside_candidate = 0
        else:
            gap, _, _, _ = gap_info
            inside_candidate = -gap

        # 4. max 계산해서 return
        return max(left_candidate, right_candidate, inside_candidate)


def solve():
    manager = StreetLightInstallation()
    q = int(input().strip())
    answer = []

    for _ in range(q):
        cmd = list(map(int, input().split()))
        order = cmd[0]

        if order == 100:
            N = cmd[1]
            M = cmd[2]
            positions = cmd[3:]
            manager.init(N, M, positions)

        elif order == 200:
            manager.add_light()

        elif order == 300:
            x = cmd[1]
            manager.remove_light(x)

        elif order == 400:
            answer.append(str(manager.query_power()))

    print("\n".join(answer))


if __name__ == "__main__":
    solve()