class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip() # 양쪽 공백 제거
        s_arr = s.split(' ') # 공백을 기준으로 리스트로 분할
        return len(s_arr[-1]) # 맨 마지막 요소의 문자열 길이 반환