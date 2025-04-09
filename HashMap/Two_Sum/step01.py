class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tbl = {}
        n = len(nums)
        for i in range(n):
           tbl[nums[i]] = i

        for i in range(n):
            complement = target - nums[i]
            if (complement in tbl) and (tbl[complement] != i):
                return [tbl[complement], i]
        return []