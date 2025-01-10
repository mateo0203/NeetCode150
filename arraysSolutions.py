from collections import defaultdict

class Solutions:
    def hasDuplicate(self, nums):
        numbersInArray = set()
        for num in nums:
            if num in numbersInArray:
                return True
            else:
                numbersInArray.add(num)
        return False

    def validAnagram(self, s: str, t:str):
        anagram = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            anagram[s[i]] += 1
            anagram[t[i]] -= 1        
        return all( value == 0 for value in anagram.values())
    
    

solution = Solutions()
result = solution.validAnagram("", "raa")
print(f"answer for input s:'' & t:'raa' is {result}")
