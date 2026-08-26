class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # freq=set()
        # for num in nums:
        #     if num in freq:
        #         return True
        #     freq.add(num)
        # return False
        freq={}

        for num in nums:
            freq[num]=freq.get(num,0)+1

        for val in freq.values():
            if val > 1:
                return True
        return False