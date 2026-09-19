class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev = {}
        for i, n in enumerate(nums):
            if n in prev:
                return True
            else:
                prev[n] = i
        return False