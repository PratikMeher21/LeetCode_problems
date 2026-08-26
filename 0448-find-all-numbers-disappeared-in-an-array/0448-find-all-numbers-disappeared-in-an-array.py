class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        li=[]

        new_nums=set(nums)

        for num in range(1,n+1):
            if num not in new_nums:
                li.append(num)
        return li
        