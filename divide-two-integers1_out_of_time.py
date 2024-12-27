class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor==1:
            return dividend
        if divisor==-1:
            res = -dividend
            if res==2147483648:
                res = 2147483647
            return res


        sign1 = 1 if dividend>=0 else -1
        sign2 = 1 if divisor>=0 else -1
        final_sign = 1 if sign1==sign2 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        cnt = 0
        while dividend>=divisor:
            print("dividend:", dividend)
            print("cnt:", cnt)

            dividend-=divisor
            cnt+=1
        
        cnt = cnt if final_sign==1 else -cnt
        return cnt