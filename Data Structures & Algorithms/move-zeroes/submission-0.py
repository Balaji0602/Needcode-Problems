class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) >= 1:
            i, j = 0, 0
            while(j < len(nums)):
                if(nums[i] != 0 and nums[j] != 0):
                    i+=1
                    j+=1
                elif(nums[j] != 0):
                    nums[i] = nums[j]
                    nums[j] = 0
                    i+=1
                    j+=1
                else:
                    j+=1
        