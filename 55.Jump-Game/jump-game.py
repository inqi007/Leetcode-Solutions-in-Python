class Solution:
    def canJump(self, nums: List[int]) -> bool:
        distance = 0
        for i in reversed(range(len(nums) - 1)):
            distance += 1
            if nums[i] >= distance:
                distance = 0
        if distance == 0:
            return True
        else:
            return False