
class Solution(object):
    def moveZeroes_timeover(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
        try 1:
        using insertion sort, time over
        """
        num_len = len(nums)
        sorted_ind = num_len
        for i in range(num_len - 1, -1, -1):
            if nums[i] == 0:
                pos = i
                while pos < sorted_ind - 1:
                    nums[pos] = nums[pos + 1]
                    pos += 1
                nums[sorted_ind - 1] = 0
                sorted_ind -= 1
    """
    try 2:
    using two pointer, passed, but also O(n^2)
    """
    def moveZeroes_passed(self, nums):
        num_len = len(nums)
        for i in range(num_len):
            if nums[i] == 0:
                for j in range(i + 1, num_len):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
    """
    Optimized -> O(n)
    """
    def moveZeroes(self, nums):
        num_len = len(nums)
        rewrite_ind = 0
        for i in range(num_len):
            if nums[i] != 0:
                nums[rewrite_ind] = nums[i]
                rewrite_ind += 1

        while rewrite_ind < num_len:
            nums[rewrite_ind] = 0
            rewrite_ind += 1



solution = Solution()
arr = [0,1,0,12,3]
solution.moveZeroes(arr)
print(arr)