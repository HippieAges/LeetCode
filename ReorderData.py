# from typing import List

class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        reordering = []
        inserted_element = False
        # print(logs)
        for log in logs:
            log_words = log.split(" ")
            # print(log_words, log)
            if log_words[1].isnumeric(): # digit logs get added to the back
                reordering.append(log)
            else:
                # print(reordering, log_words)
                reordering_len = len(reordering)
                if reordering_len == 0 or (reordering_len > 0 and reordering[0][-1].isnumeric()): # if we only have digit logs, add the letter log
                    reordering.insert(0, log)
                else:
                    content = " ".join(log_words[1:])
                    for index, ordering in enumerate(reordering):
                        order = ordering.split(" ")
                        identifier = order[0]
                        words = " ".join(order[1:])
                        # print(reordering)
                        if content < words or order[1].isnumeric() or (content == words and log_words[0] < identifier): 
                            reordering.insert(index, log)
                            inserted_element = True
                            break
                    if not inserted_element:
                        reordering.append(log)
                    inserted_element = False
        return reordering

    # another solution that provides an identical runtime to my previous solution 
    def newReorder(self, logs: list[str]) -> list[str]:

        def order(log: str) -> tuple:
            identifier, content = log.split(' ', maxsplit=1)
            return (1, ) if content[0].isnumeric() else (0, content, identifier)
        return sorted(logs, key=order)


s = Solution()
# print(s.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
# print(s.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
print(s.reorderLogFiles(["j je", "b fjt", "7 zbr", "m le", "o 33"]))
print(s.newReorder(["j je", "b fjt", "7 zbr", "m le", "o 33"]))
print(s.newReorder(s.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"])))