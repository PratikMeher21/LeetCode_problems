class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst():
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] >= target:
                    ans=mid
                    right=mid-1
                else:
                    left=mid+1

            return ans

        def findLast():
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] <= target:
                    ans=mid
                    left=mid+1
                else:
                    right=mid-1 

            return ans

        first = findFirst()

        if first == -1 or nums[first] != target:
            return [-1, -1]

        return [findFirst(), findLast()]