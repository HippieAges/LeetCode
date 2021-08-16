class Solution:
    def compress(self, chars: List[str]) -> int:
        
        if (chars_len := len(chars)) == 1:
            return chars_len
        
        s = ""
        left = 0
        count = 0
        
        for right in range(len(chars)):
            if chars[left] != chars[right]:
                
                if count == 1:
                    s += f"{chars[left]}"
                    left = right
                else:
                    if count <= 9:
                        s += f"{chars[left]}{count}"
                    else: # count >= 10
                        count_len = len(str(count)) - 1
                        s += f"{chars[left]}"
                        while count_len >= 0:
                            s += str(count // (10**count_len))
                            count = int(str(count)[1:]) if count_len > 0 else count
                            count_len -= 1
                
                count = 1
                left = right
            else:
                count += 1
        if right == len(chars) - 1:
            s += f"{chars[right]}"
            if count != 1:
                s += f"{count}"
            
        
        # iterate over chars to update it & then remove the extra elements on the end
        for idx, c in enumerate(s):
            chars[idx] = c
        
        while len(chars) != len(s):
            chars.pop()
        
        return len(chars)