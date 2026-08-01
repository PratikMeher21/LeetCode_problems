class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left=0
        right=0

        arr=[]

        while left < len(nums1) and right< len(nums2):
            if nums1[left] <= nums2[right]:
                arr.append(nums1[left])
                left+=1
            else:
                arr.append(nums2[right])
                right+=1 
        while right < len(nums2):
            arr.append(nums2[right])
            right+=1
        while left < len(nums1):
            arr.append(nums1[left])
            left+=1
        left=0
        right=len(arr)-1
        while left < right :
            left+=1
            right-=1
        if len(arr) < 2:
            return arr[0]
        return (arr[left] + arr[right]) /2
                