class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        first_values = []

        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                first_values.append(matrix[i][j])

                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = tmp

        reversed_first_values = first_values[::-1]
        return reversed_first_values

matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = Solution().rotate(matrix)
print("Rotated matrix:", matrix)
print("Reversed first values:", result)