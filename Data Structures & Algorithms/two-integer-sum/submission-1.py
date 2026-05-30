class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for ind in range(len(nums)):
            remaining = target - nums[ind]
            if hash_map.get(remaining) is not None:
                return [hash_map.get(remaining), ind]
            else:
                hash_map[nums[ind]] = ind   
        return []
        