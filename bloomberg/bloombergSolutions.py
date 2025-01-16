from collections import Counter
class Solutions:
    def twoSum(self, nums: list[int], target:int):
        pass

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        Output: [1,2,2,3,5,6]
        Explanation: The arrays we are merging are [1,2,3] and [2,5,6].

        #To avoid shifting, start sorting from the right to the left
        """
        currM = m - 1
        currN = n - 1
        currL = len(nums1) - 1
        while currM > -1 and currN > -1:
            if nums1[currM] > nums2[currN]:
                nums1[currL] = nums1[currM]
                currM -= 1
                currL -= 1
            else:
                nums1[currL] = nums2[currN]
                currN -= 1
                currL -= 1
        while currM > -1:
                nums1[currL] = nums1[currM]
                currM -= 1
                currL -= 1

        while currN > -1:
                nums1[currL] = nums2[currN]
                currN -= 1
                currL -= 1
        return nums1
    

    def maxProfit(self, prices: List[int]) -> int:
        """
        Input: prices = [7,1,5,3,6,4]
        Output: 5
        Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
        Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

        Approach
        - Set a left and right pointer - where left is the day I buy and right the day I sell


        Analysis: O(n) time complexity and O(1) space complexity
        """
        maxProfit = 0
        leftP = 0
        rightP = 1
        while rightP < len(prices):
            if prices[rightP] < prices[leftP]:
                leftP = rightP
                rightP += 1
            else:
                currProfit = prices[rightP] - prices[leftP]
                maxProfit = max(currProfit, maxProfit)
                rightP += 1
        return maxProfit
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Find the start and end bounds
        startIdx = self.findBound(nums, target, isLeft=True)
        if startIdx == -1:  # Target not found
            return [-1, -1]
        
        endIdx = self.findBound(nums, target, isLeft=False)
        return [startIdx, endIdx]

    def findBound(self, nums, target, isLeft: bool) -> int:
        start, end = 0, len(nums) - 1
        bound = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                bound = mid
                if isLeft:
                    end = mid - 1  # Keep searching left
                else:
                    start = mid + 1  # Keep searching right
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return bound

    def equalFrequency(self, word):
         # Count the frequency of each character
        counter = Counter(word)
        keys = list(counter.keys())  # Collect keys beforehand to avoid modifying the dictionary during iteration

        for letter in keys:
            # Decrease the frequency of the current letter
            counter[letter] -= 1
            if counter[letter] == 0:
                del counter[letter]  # Remove the letter if frequency is zero
            
            # Get the unique frequencies of the remaining letters
            freq_set = set(counter.values())
            
            # Check if the unique frequencies are valid
            if len(freq_set) == 1:  # All frequencies are the same
                return True
            
            # Restore the original frequency of the letter
            if letter in counter:
                counter[letter] += 1
            else:
                counter[letter] = 1  # Re-add the letter if it was removed
        
        return False
    
