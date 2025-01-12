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