class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s) 
        t_len = len(t)
        t_start = 0 # loop 돌 때, t 시작점을 지정할 변수

        idx = 0 # s_len과 비교할 변수 (결과를 판단할 변수)
        result = False # 결과 변수

        for i in range(s_len):
            for j in range(t_start, t_len):
                if s[i] == t[j]:
                    idx += 1
                    t_start = j+1
                    break

        if(s_len == idx):
            result = True

        return result
        