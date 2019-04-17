class Solution:
    def minDeletionSize(self, A: list) -> int:
        lenX = len(A)
        lenY = len(A[0])
        num = 0
        for j in range(lenY):
            for i in range(lenX-1):
                if A[i][j] <= A[i+1][j]:
                    continue
                else:
                    num += 1
                    break
        return num
A = ["rrjk","furt","guzm"]
re = Solution().minDeletionSize(A)
print(re)





