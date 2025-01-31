class Solutions:
    def validPalindrome(self, s: str):
        if len(s) == 0:
            return True
        leftP = 0
        rightP = len(s) - 1
        while leftP < rightP:
            # Skip non-alphanumeric characters
            if not s[leftP].isalnum():
                leftP += 1
                continue
            if not s[rightP].isalnum():
                rightP -= 1
                continue
            # Compare characters
            if s[leftP].lower() != s[rightP].lower():
                return False
            leftP += 1
            rightP -= 1
        return True

    def twoSumTwo(self, numbers: list[int], target: int) -> list[int]:
        leftP = 0
        rightP = len(numbers) - 1

        while leftP < rightP:
            currSum = numbers[leftP] + numbers[rightP]
            if currSum == target:
                return [leftP+1, rightP+1]
            elif currSum > target:
                rightP -= 1
            else:
                leftP += 1

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        """
        #input: words (string array)

        such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.
        Return an integer denoting the number of index pairs (i, j) 

        Example: ["a","aba","ababa","aa"] -- brute force O(n^2*avg_str_size)

        """

        counter = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    counter += 1
        return counter
    
    def isPrefixAndSuffix(self, word1, word2):
        if word1 > word2:
            return False
        elif word2.startswith(word1) and word2.endswith(word1):
            return True