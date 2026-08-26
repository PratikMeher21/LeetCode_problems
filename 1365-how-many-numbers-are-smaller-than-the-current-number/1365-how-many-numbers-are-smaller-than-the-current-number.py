class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums= sorted(nums)

        freq={}

        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in freq:
                freq[sorted_nums[i]] = i

        res=[]
        for num in nums:
            res.append(freq[num])
        return res
        