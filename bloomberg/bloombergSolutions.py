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
    

    def maxProfit(self, prices: list[int]) -> int:
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
    
    def searchRange(self, nums: list[int], target: int) -> list[int]:
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
    def stringMatching(self, words):
        #Input: array of strings
        #return all strings in words that is a substring of another words
        result = set()
        for word in words:
            for wordT in words:
                if wordT == word:
                    continue
                else:
                    if word in wordT:
                        result.add(word)
        return list(result)

    def countPalindromicSubsequence(self, s: str) -> int:
        if len(s) == 0:
            return []
        if len(s) == 1:
            return [s]
        
        result = 0
        leftSet = set()
        rightDict = dict()
        visited = set()
        #create the rightDict
        for i in range(1, len(s)):
            try:
                rightDict[s[i]] += 1
            except:
                rightDict[s[i]] = 1

        for i in range(1,len(s)):
            rightDict[s[i]] -= 1
            if rightDict[s[i]] == 0:
                del rightDict[s[i]]
            leftSet.add(s[i-1])
            for letter in leftSet:
                if letter in rightDict:
                    if letter + s[i] + letter not in visited:
                        result += 1
                        visited.add(letter + s[i] + letter)
        return result

    def subsets(self, nums: list[int]) -> list[list[int]]:
        #backtracking approach of choosing or not choosing an Option
        #[1, 2, 3]
        if len(nums) == 0:
            return []
        res = []
        res += self.dfs(nums, [], 0)
        return res
    
    def dfs(self, nums, subset, index):
        res = []
        if index >= len(nums):
            return [subset]
        subsetA = subset + [nums[index]]
        res += self.dfs(nums, subsetA, index+1)
        res += self.dfs(nums, subset, index+1)
        return res
    
    def subsequences(self, aStr: str) -> list[str]:
        if len(aStr) == 0:
            return []
        res = []
        return sorted(res + self.dfsS(aStr, "", 0))

    def dfsS(self, aStr, subseq, index):
        res = []
        if index >= len(aStr):
            return [subseq]
        subseqA = subseq + aStr[index]
        res += self.dfsS(aStr, subseqA, index+1)
        res += self.dfsS(aStr, subseq, index+1)
        return res

    "abcde" 