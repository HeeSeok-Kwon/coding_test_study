class Solution:
    def isHappy(self, n: int) -> bool:
        # 결과 변수
        result = False
        # 계산 결과를 담을 변수
        square_sum_set = set()
        # 제곱 값을 담을 배열 변수
        square_arr = []

        while True:
            square_arr = []
            # 각 자리의 숫자 가져오기
            while n > 0:
                digit = n % 10
                square_digit = digit * digit
                square_arr.append(square_digit)
                n //= 10
            
            square_sum = sum(square_arr)
            
            if square_sum in square_sum_set:
                result = False
                break 
            if square_sum == 1:
                result = True
                break

            square_sum_set.add(square_sum)

            n = square_sum
        
        return result