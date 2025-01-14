class Solutions:
    def maxProductSubarray(self, nums: list[int]):
        """
        Given an integer array `nums`, find the contiguous subarray within the array 
        (containing at least one number) that has the largest product and return its product.

        Parameters:
            nums (list[int]): A list of integers which can include positive, negative, and zero values.

        Returns:
            int: The maximum product of a contiguous subarray.

        Example:
            Input: nums = [2, 5, -2, 4, 4, 0, 3, 4] -------   [2] -> [2, 5] -> [2, 5, -2, 4, 4, -2] max:[-160, 16], cont:[-160, 16]
            Output: 6

            Input: nums = [-2, 0, -1]
            Output: 0

        Problem Analysis:
            - We are just returning the product of the subarray
            - Zero cannot be included in the subarray, unless they are all zeroes
            - Positive nums will always lead to the largest subarray
            - Negatives depend if even num of negatives or odd num of negatives

            - Adding more numbers to the array, either gets the largest product or the smallest product

        
        Approach:
            - Following a dp approach
            - Keep track of the largest +&- product within subarrays and of the contiguous +&- product within subarrays.
            - Modify both groups of vars progressively

            - If number is positive: Increase both contiguous

            - If number is negative: largestPos becomes negative and smallestPos becomes positive

            -If number is zero:Start over
        """

        # Initialize variables
        largestProduct = float('-inf')  # Global maximum product
        largestContProduct = 1  # Current positive product
        smallestContProduct = 1  # Current negative product

        for num in nums:
            if num == 0:
                # Reset contiguous products on zero
                largestContProduct = 1
                smallestContProduct = 1
                largestProduct = max(largestProduct, 0)  # Zero may be the largest product
                continue
            elif num > 0:
                # Positive number: update both positive and negative products
                largestContProduct = max(largestContProduct * num, num)
                smallestContProduct = min(smallestContProduct * num, num)
            else:
                # Negative number: swap positive and negative products
                temp = largestContProduct
                largestContProduct = max(smallestContProduct * num, num)
                smallestContProduct = min(temp * num, num)

            # Update the global maximum product
            largestProduct = max(largestProduct, largestContProduct)

        return largestProduct
    
    def canJump(self, nums: list[int]):
        """
        You are given an integer array nums. You are initially positioned at the array's first index, 
        and each element in the array represents your maximum jump length at that position.
        Return true if you can reach the last index, or false otherwise.

        Example:
        input = [2, 4, 1, 0, 1], Expected = True
        Input: nums = [3,2,1,0,4] Output: False


        Problem Analysis: 
        - 0 are the issues in here
        - Break down the problem Top-Down: If I can reach the destination from an ith index and I can reach i from a jth index, 
            then I can reach the destination from the jth index
        """

        #DP Approach
        if len(nums) == 1:
            return True

        dp = [float('inf') for i in range(len(nums))]
        dp[len(nums) - 1] = 0
        for i in range(len(nums) - 2, -1, -1):
            jumps = nums[i]
            if jumps == 0:
                continue
            for jump in range(1,jumps+1):
                if i + jump < len(nums) and dp[i + jump]:
                    dp[i] = min(dp[i + jump] + 1, dp[i])
        return dp[0]
    
    def canJumpOpt(self, nums: list[int]):
        farthest = 0
        l = 0
        r = 0
        jumps = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, nums[i] + i)
            l = r+1
            r = farthest
            jumps += 1
        return jumps

    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        #I will need to save a cache with the prev calculated results
        result = []
        cache = {}
        for i in range(lo, hi+1):
            counter = self.getPower(i, cache)
            cache[i] = counter
            result.append((counter, i))
        result.sort()
        return result[k-1][1]
    
    def getPower(self, num, cache):
        curr = num
        counter = 0
        while curr != 1:
            if curr in cache:
                return counter + cache[curr]
            if curr % 2 == 0:
                curr = curr/2
            else:
                curr = 3 * curr +1
            counter += 1
        return counter