from twoPointersSolutions import Solutions
class Tests:
    def __init__(self):
        self.solution = Solutions()
    
    def testValidPalindrome(self):
        test_cases = [
            {"input": "asa", "expected": True},
            {"input": "", "expected": True},
            {"input": "polit", "expected": False}
        ]

        for i, test_case in enumerate(test_cases):
            input = test_case["input"]
            expected = test_case["expected"]
            result = self.solution.validPalindrome(input)
            assert result == expected, print(f"Test case number: {i + 1} failed, with input: {input} result should be {expected}, but was {result}")
            print(f"Test case number: {i + 1} passed")

tests = Tests()
tests.testValidPalindrome()
