class Solution:
    def validMountainArray(self, A: list) -> bool:
        L = len(A)
        if L < 3:
            return False
        if A[0] < A[1]:
            start = 1
        else:
            return False
        for i in range(1, L-1):
            if start == 1 and A[i] < A[i+1]:
                continue
            elif start == 1 and A[i] > A[i+1]:
                start = 2
                continue
            elif start == 2 and A[i] > A[i+1]:
                continue
            else:
                return False
        if start == 1:
            return False
        return True

A = [0,2,6,9,69,85,21,3,0,5]
result = Solution().validMountainArray(A)
print(result)