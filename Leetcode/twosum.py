class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_index = {}
        for index, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in num_index:
                return [num_index[num2], index]
            num_index[num1] = index
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([3, 2, 4], 6))
print(solution.twoSum([3, 3], 6))