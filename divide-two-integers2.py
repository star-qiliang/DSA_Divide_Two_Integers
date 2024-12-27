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
        int_divisor = divisor
        dividend = str(dividend)
        divisor = str(divisor)
        
        stack = ""
        res_list = []
        for x in dividend:
            cnt = 0
            stack+=x
            # print("stack:", stack)
            while int(stack)>=int_divisor:
                # print("cnt:", cnt)
                stack = str(int(stack)-int_divisor)
                cnt+=1

            res_list.append(str(cnt))
            # print("cnt", cnt)

        # print("res_list:", res_list)

        res = int(''.join(res_list))*final_sign
        return res