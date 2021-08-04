from random import choices
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.enumerated_w = [(idx, self.w[idx]) for idx in range(len(self.w))]
        self.w_sum = sum(w)
        self.weights = [curr_weight / self.w_sum * 100 for curr_weight in w]

    def pickIndex(self) -> int:
        element = choices(self.enumerated_w, weights = self.weights)[0][0]
        return element


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()