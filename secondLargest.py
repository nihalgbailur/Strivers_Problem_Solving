class Solution:
    def secondLargestElement(self, nums):
        largest = nums[0]
        second = float("-inf")

        for x in nums[1:]:
            if x > largest:
                second = largest
                largest = x
            elif largest > x > second:
                second = x

        if second == float("-inf"):
            return -1
        return second
