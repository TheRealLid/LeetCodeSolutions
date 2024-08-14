from typing import List, Callable

# 1. Two Sum
# Brute Force
def twoSum_brute(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
# Optimized one pass
def twoSum_onePass(nums: List[int], target: int) -> List[int]:
    compliments = {}
    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in compliments:
            return [compliments[compliment], i]
        compliments[nums[i]] = i     
    return []   

# Accepts any implementation of TwoSum and tests a couple cases to validate it is functional
def testTwoSum(twoSum:Callable[[List[int],int],List[int]]):
    case_1 = [2,7,11,15]
    trgt_1 = 9
    case_2 = [3,2,4]
    trgt_2 = 6
    case_3 = [3,3]
    trgt_3 = 6

    # Assertions
    assert twoSum(case_1, trgt_1) == [0, 1], f"Test case 1 failed: {twoSum(case_1, trgt_1)}"
    assert twoSum(case_2, trgt_2) == [1, 2], f"Test case 2 failed: {twoSum(case_2, trgt_2)}"
    assert twoSum(case_3, trgt_3) == [0, 1], f"Test case 3 failed: {twoSum(case_3, trgt_3)}"
    print("All test cases passed!")

# Run tests with twoSum_brute
print("Testing twoSum_brute:")
testTwoSum(twoSum_brute)

# Run tests with twoSum_onePass
print("Testing twoSum_onePass:")
testTwoSum(twoSum_onePass)

# 9. Palindrome Number
def isPalindrome(x: int) -> bool:
    word = str(x)
    n = len(word)
    for i in range(int(n/2)):
        if word[i] != word[n-i-1]:
            return False
    return True

def testIsPalindrome(isPalindrome: Callable[[int], bool]):
    case_1 = 121
    case_2 = -121
    case_3 = 10
    case_4 = -10
    case_5 = 11

    # Assertions
    assert isPalindrome(case_1) == True, f"Test case 1 failed: {isPalindrome(case_1)}"
    assert isPalindrome(case_2) == False, f"Test case 2 failed: {isPalindrome(case_2)}"
    assert isPalindrome(case_3) == False, f"Test case 3 failed: {isPalindrome(case_3)}"
    assert isPalindrome(case_4) == False, f"Test case 4 failed: {isPalindrome(case_4)}"
    assert isPalindrome(case_5) == True, f"Test case 5 failed: {isPalindrome(case_5)}"
    print("All palindrome test cases passed!")

# Run tests with isPalindrome
print("Testing isPalindrome:")
testIsPalindrome(isPalindrome)