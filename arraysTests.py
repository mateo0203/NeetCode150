from arraysSolutions import Solutions

class Tests:
    def __init__(self):
        self.solution = Solutions()  # Initialize the solution instance here

    def test_hasDuplicate(self):
        test_cases = [
            {"input": [1, 2, 3, 4, 5], "expected": False},  # No duplicates
            {"input": [1, 2, 3, 4, 5, 3], "expected": True},  # Duplicate 3
            {"input": [1, 1], "expected": True},  # Single duplicate (1)
            {"input": [], "expected": False},  # Empty array
            {"input": [42], "expected": False},  # Single element
            {"input": [5, 5, 5, 5, 5], "expected": True},  # All duplicates
        ]

            
        # Run test cases
        for i, test_case in enumerate(test_cases):
            nums = test_case["input"]
            expected = test_case["expected"]
            result = self.solution.hasDuplicate(nums)  # Call on the instance
            assert result == expected, f"Test case {i+1} failed: Input {nums} | Expected {expected} | Got {result}"
            print(f"Test case {i+1} passed: Input {nums} | Output {result}")
    
    def test_validAnagram(self):
        test_cases = [
            {"input":("ara","raa"), "expected": True},
            {"input":("","raa"), "expected": False},
            {"input":("",""), "expected": True},
            {"input":("ksk",""), "expected": False},
            {"input":("ksk","kska"), "expected": False},
            {"input":("aaa","aaa"), "expected": True}
        ]

        
        for i, test_case in enumerate(test_cases):
            s = test_case["input"][0]
            t = test_case["input"][1]
            expected = test_case["expected"]
            result = self.solution.validAnagram(s,t)
            assert result == expected, f"Test case {i+1} failed: Input s:{s} and t:{t} | Expected {expected} | Got {result}"
            print(f"Test case {i+1} passed: Input s:{s} and t:{t}  | Output {result}")

    def test_twosum(self):
        test_cases = [
            {"input":([2, 6, 4], 8), "expected": []},
            {"input":([2, 6, 4], 8), "expected": False},
            {"input":([2, 6, 4], 8), "expected": True},
            {"input":([2, 6, 4], 8), "expected": False},
            {"input":([2, 6, 4], 8), "expected": False},
            {"input":([2, 6, 4], 8), "expected": True}
        ]
    


# Run the tests
tests = Tests()
print("Working unit tests for hasDuplicates...")
tests.test_hasDuplicate()

print("Working unit tests for validAnagram...")
tests.test_validAnagram()