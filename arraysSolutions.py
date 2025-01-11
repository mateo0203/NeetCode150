from collections import defaultdict, Counter
import heapq

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
    
    def twoSum(self, list: list[int], target: int):
        # [2, 4, 6], target : 8
        # 6 + 2
        aDict = {}
        for i in range(len(list)):
            curr = list[i]
            if curr in aDict:
                return [i, aDict[curr]]
            
            complement = target - curr
            aDict[complement] = i
        return False

    def topFrequentKElements(self, nums: list[int], k:int):
        #get the frequency table O(n)
        counter = Counter(nums)
        heap = [(-freq, num) for  num, freq in counter.items()]
        heapq.heapify(heap)

        #Heap creation O(nlogn)
        result = []

        #return result list O(k)
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
    
        #Even faster would be to create a minheap of fixed size k, so then the iterations would be nlogk
    
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        #What they are asking:
        #Given nums return output list, so that each output[i] is the product of all elements in nums except num[i]

        #brute force -> for each num in nums: for each other num in nums, multiply them and fill output
        #O(n^2) -- assuming multiplication takes O(1)

        #Example input: [6, 2, 5, 3, 1]
        #Output: []

        #With division, trivial way would be:
        #Iterate once through array to get total product: O(n)
        #Iterate again through array and build resultant array dividing by the nums[i] in each iteration: O(n)

        #Why that doesn't work ? I didn't pay attention to when we are dealing with zeroes:
        #zero -- doesn't work
        # How to deal with cases with zeroes:
            # If other zero, then totalProduct is 0
            # If not other zero, then totalProduct is totalProduct  

        #More than one zero in array    
        totalProduct = 1
        zeroCount = 0
        for num in nums:
            if num == 0:
                zeroCount += 1
                continue
            totalProduct *= num
        if zeroCount > 1:
            return [0 for i in range(len(nums)) ]
        result = []
        for num in nums:
            if num == 0:
                result.append(int(totalProduct))
            else:
                if zeroCount == 1:
                    result.append(0)
                else:
                    result.append(int(totalProduct/num))
        return result
    
    #Resultant time complexity would be:
        #O(n) runtime to get the totalProduct + O(n) runtime to build the resultant array
        #Final big O = O(n)
    #Resultant space complexity would be:
        #O(n) space to build the resultant array
        #Final space complexity = O(n) 
        

    def productExceptSelfFollowUp(self, nums: list[int]) -> list[int]:
        #Same question as the above, but without using division operation

        #I could change the division operation to some kind of binary operation, but would that still be O(1)?
        #The above is not valid, because bitwise operations would only be better if I use powers of two

        #More brainstorm:
        #input = [7, 4, 3, 6, 1, 2]
        #prefix = [1, 7, 28, 84, 504, 504]
        #suffix = [144, 36, 12, 2, 2, 1]

        #multiply both products

        #build prefix array
        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(prefix[-1] * nums[i - 1])
        
        suffix = []
        for i in range(len(nums) - 1,-1,-1):
            if i == len(nums) - 1:
                suffix = [1]
            else:
                suffix.append(suffix[-1] * nums[i + 1])
                prefix[i] = suffix[-1]*prefix[i]
    
        return prefix
        

solution = Solutions()
result = solution.validAnagram("", "raa")
print(f"answer for input s:'' & t:'raa' is {result}")
