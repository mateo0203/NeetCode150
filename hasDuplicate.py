class Solution:
    def hasDuplicate(nums):
        numbersInArray = set()
        for num in nums:
            if num in numbersInArray:
                return True
            else:
                numbersInArray.add(num)
        return False
