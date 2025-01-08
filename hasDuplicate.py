class Solution:
    def hasDuplicate(self, nums):
        numbersInArray = set()
        for num in nums:
            if num in numbersInArray:
                return True
            else:
                numbersInArray.add(num)
        return False

# Custom testing code
def test_hasDuplicate():
    test_cases = [
        {"input": [1, 2, 3, 4, 5], "expected": False},  # No duplicates
        {"input": [1, 2, 3, 4, 5, 3], "expected": True},  # Duplicate 3
        {"input": [1, 1], "expected": True},  # Single duplicate (1)
        {"input": [], "expected": False},  # Empty array
        {"input": [42], "expected": False},  # Single element
        {"input": [5, 5, 5, 5, 5], "expected": True},  # All duplicates
    ]
    
    # Create an instance of Solution
    solution = Solution()
    
    # Run test cases
    for i, test_case in enumerate(test_cases):
        nums = test_case["input"]
        expected = test_case["expected"]
        result = solution.hasDuplicate(nums)  # Call on the instance
        assert result == expected, f"Test case {i+1} failed: Input {nums} | Expected {expected} | Got {result}"
        print(f"Test case {i+1} passed: Input {nums} | Output {result}")

# Run the tests
test_hasDuplicate()