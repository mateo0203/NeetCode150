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

        #Insert into a data structure as a tuple (freq, num) 

        #Sort the data structure and return the top k

        #If we use the approach of a list then O(n) for appending to list list and O(nlogn) for sorting it with timsort and O(k) to retrieve from heap
        #Total runtime: O(n) + O(n) + O(nlogn) + O(k)[we think of this as insignificant because n approaches infinity while k doesnt]
        #Total space: O(n) [counter dict] + O(n) [list] + 0(k) [return list]
        #if we use the approach of a heap then O(nlogn) for appending to heap and O(k) to retrieve from heap
        
        #Total runtime: O(n) + O(nlogn) + 0(klogn)
        #Total space: O(n) [counter dict] + 0(n) heap + 0(k) [return list]
        #Conclusion: use a heap

        #Heap creation with heapify O(n)
        heap = [(-freq, num) for  num, freq in counter.items()]
        heapq.heapify(heap)

        #Heap creation O(nlogn)
        result = []

        #return result list O(k)
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
    
        #Even faster would be to create a minheap of fixed size k, so then the iterations would be nlogk

        


        

solution = Solutions()
result = solution.validAnagram("", "raa")
print(f"answer for input s:'' & t:'raa' is {result}")
