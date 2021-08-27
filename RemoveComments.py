class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res, buff, isOpen = [], "", False
        for comment in source: 
            i, n = 0, len(comment)
            while i < len(comment):
                if comment[i:i + 2] == "//" and not isOpen:
                    break
                elif comment[i:i + 2] == "/*" and not isOpen:
                    isOpen = True
                    i += 1
                elif comment[i:i + 2] == "*/" and isOpen: 
                    isOpen = False
                    i += 1
                elif not isOpen:
                    buff += comment[i]
                i += 1
            if buff and not isOpen:
                res.append(buff)
                buff = ""
        return res