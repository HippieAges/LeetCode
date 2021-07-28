class Solution:
    def isArmstrong(self, n: int) -> bool:
        
        # mathy solution
        def get_length() -> int:
            count = 0
            temp_n = n
            while temp_n != 0:
                count += 1
                temp_n //= 10
            return count
        
        k = get_length()
        print(k)
        result = 0
        temp_n = n
        while temp_n != 0:
            result += (temp_n % 10)**k
            temp_n //= 10
        print(result)
        
          # string solution, fastest solution
#         str_n = str(n)
#         k = len(str_n)
#         result = 0
        
#         for character in str_n:
#             result += int(character)**k
            
        return result == n