class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()        
        for i in range(1,len(nums)):
            #for j in range(i+1,len(nums)):
                #print(i,j)
            if nums[i]==nums[i-1]:
                return True
        return False
