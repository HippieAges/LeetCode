from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        # keep a stack that stores information regarding open characters
        # if we ever have a closing character that doesn't correspond to the head stack character, then return False
        # otherwise, if we have the corresponding closing brace, pop of the stack and continue
        # otherwise, add the other type of opening character to the top of the stack
        
        stack = deque()
        
        for character in s:
            last_in = len(stack) - 1
            current_char = ord(character)

            if len(stack) == 0:
                stack.append(character)
            elif character != '(' and character != '{' and character != '[' and \
                 ord(stack[last_in]) + 1 != current_char and ord(stack[last_in]) + 2 != current_char: 
                print(stack[0], character)
                return False
            elif ord(stack[last_in]) + 1 == current_char or ord(stack[last_in]) + 2 == current_char:
                stack.pop()
            else:
                stack.append(character)
                
        return True if len(stack) == 0 else False