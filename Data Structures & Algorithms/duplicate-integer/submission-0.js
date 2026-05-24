class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const resp = [...new Set(nums)];
        return nums.length != resp.length
    }
}
