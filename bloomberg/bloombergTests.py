import bloombergSolutions
class Tests:

    def __init__(self):
        pass

    def testSubsequences(self, aStr):
        solution = bloombergSolutions.Solutions()
        print(solution.subsequences(aStr))


if __name__ == "__main__":
    tests = Tests()
    tests.testSubsequences("abcde")
    print("I run here")