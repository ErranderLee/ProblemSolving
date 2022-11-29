class Solution(object):

    def rec(self, digits, nth):
        global flag
        if nth < 0:
            flag = 1
            return
        if digits[nth] == 9:
            digits[nth] = 0
            self.rec(digits, nth - 1)
        else:
            digits[nth] += 1
            flag = 0
            return


    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        global flag
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            self.rec(digits, len(digits) - 1)
            if flag == 1:
                return [1] + digits
            return digits

    def plusOne_optimized(self, digits):
        num = "".join([str(element) for element in digits])
        num = int(num) + 1
        return list(str(num))

solution = Solution()
result = solution.plusOne([8,9,9,9])
print(result)


