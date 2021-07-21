class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # for loop that goes up to n * n
        # have two variables, i and j, j = i in the beginning, then j = (j + 1) % n
        # i increments when the above condition of j = (j + 1) % n is true
        # use these two variables to switch places for the two elements, i.e. matrix[i][j] = matrix[j][i]
        matrix.reverse()
        i, j = 0, 0
        n = len(matrix)
        for _ in range(n * n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            if (j + 1) % n == 0:
                i += 1
                j = i
                if i == n:
                    break
            else:
                j += 1