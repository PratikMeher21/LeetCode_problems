class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def backtracking(path):
            if len(nums) == len(path):
                res.append(path[:])
                return
            
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtracking(path)
                    path.pop()

        backtracking([])
        return res
        