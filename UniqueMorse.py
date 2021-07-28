class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letter_to_morse = {
                            "a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..",
                           "j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-."
                           ,"s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."
                          }
        transformation_morse = set()
        
        all_words = ""
        for word in words:
            all_words += f"{word}|"
            
        transformation = ""
        for character in all_words:
            if character != "|":
                transformation += letter_to_morse[character]
            else:
                transformation_morse |= {transformation}
                transformation = ""
            
        return len(transformation_morse)