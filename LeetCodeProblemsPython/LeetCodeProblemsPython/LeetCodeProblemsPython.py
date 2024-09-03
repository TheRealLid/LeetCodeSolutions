from typing import List, Callable

#####################  1. Two Sum #################### 
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

print("Testing twoSum_brute:")
testTwoSum(twoSum_brute)

print("Testing twoSum_onePass:")
testTwoSum(twoSum_onePass)

#####################################################################################

#####################  9. Palindrome Number #################### 
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

def romanToInt(s: str) -> int:
    myDict = {'I':1, 'V':5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    for i in range(len(s)):
        if i < len(s) - 1 and myDict[s[i]] < myDict[s[i+1]]:
            ans -= myDict[s[i]]
        else:
            ans += myDict[s[i]]
    return ans
def testRomanToInt(romanToInt: Callable[[str], int]):
    case_1 = "III"
    case_2 = "IV"
    case_3 = "IX"
    case_4 = "LVIII"
    case_5 = "MCMXCIV"

    # Assertions
    assert romanToInt(case_1) == 3, f"Test case 1 failed: {romanToInt(case_1)}"
    assert romanToInt(case_2) == 4, f"Test case 2 failed: {romanToInt(case_2)}"
    assert romanToInt(case_3) == 9, f"Test case 3 failed: {romanToInt(case_3)}"
    assert romanToInt(case_4) == 58, f"Test case 4 failed: {romanToInt(case_4)}"
    assert romanToInt(case_5) == 1994, f"Test case 5 failed: {romanToInt(case_5)}"
    
    print("All Roman to Integer test cases passed!")

# Run tests with romanToInt
print("Testing romanToInt:")
testRomanToInt(romanToInt)

#####################################################################################

#################### 14. Longest Common Prefix #################### 
# Brute Force
def longestCommonPrefix(strs: List[str]) -> str:
    counter = 0
    shortestStr = strs[0]
    for word in strs:
        if len(word) < len(shortestStr):
            shortestStr = word
    for char in shortestStr:
        for word in strs:
            if word[counter] != char:
                return shortestStr[:counter]
        counter += 1
    return shortestStr[:counter]

# sorted, compare first and last
def longestCommonPrefix_Smart(strs: List[str]) -> str:
    ans = ""
    sortedList = sorted(strs)
    first = sortedList[0]
    last = sortedList[-1]
    for i in range(min(len(first),len(last))):
        if first[i] != last[i]:
            return ans
        else:
            ans+= first[i]
    return ans

def testLongestCommonPrefix(longestCommonPrefix: Callable[[List[str]], str]):
    case_1 = ["flower","flow","flight"]
    case_2 = ["dog","racecar","car"]
    case_3 = ["interview","interstate","internet"]
    case_4 = ["a"]
    case_5 = ["geeks", "geek", "gee", "ge"]

    # Assertions
    assert longestCommonPrefix(case_1) == "fl", f"Test case 1 failed: {longestCommonPrefix(case_1)}"
    assert longestCommonPrefix(case_2) == "", f"Test case 2 failed: {longestCommonPrefix(case_2)}"
    assert longestCommonPrefix(case_3) == "inter", f"Test case 3 failed: {longestCommonPrefix(case_3)}"
    assert longestCommonPrefix(case_4) == "a", f"Test case 4 failed: {longestCommonPrefix(case_4)}"
    assert longestCommonPrefix(case_5) == "ge", f"Test case 5 failed: {longestCommonPrefix(case_5)}"
    
    print("All Longest Common Prefix test cases passed!")

print("Testing longestCommonPrefix:")
testLongestCommonPrefix(longestCommonPrefix)
testLongestCommonPrefix(longestCommonPrefix_Smart)



#####################################################################################

#################### 20. Valid Parentheses #################### 

def isValid(s: str) -> bool:
    stack = []
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}
    for char in s:
            # If char is a left handed Parentheses
        if char in bracket_pairs:
            stack.append(char)
        else:
            # if stack is empty or the top element isnt the correct parentheses
            if not stack or bracket_pairs[stack.pop()] != char: 
                return False

    return not stack

def testIsValid(isValid: Callable[[str], bool]):
    case_1 = "()"
    case_2 = "()[]{}"
    case_3 = "(]"
    case_4 = "([)]"
    case_5 = "{[]}"

    # Assertions
    assert isValid(case_1) == True, f"Test case 1 failed: {isValid(case_1)}"
    assert isValid(case_2) == True, f"Test case 2 failed: {isValid(case_2)}"
    assert isValid(case_3) == False, f"Test case 3 failed: {isValid(case_3)}"
    assert isValid(case_4) == False, f"Test case 4 failed: {isValid(case_4)}"
    assert isValid(case_5) == True, f"Test case 5 failed: {isValid(case_5)}"
    
    print("All isValid test cases passed!")

testIsValid(isValid)


#####################################################################################

#################### 21. Merge Two Sorted Lists #################### 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def testMergeTwoLists(mergeTwoLists: Callable[[ListNode, ListNode], ListNode]):
    print(f"Testing function: {mergeTwoLists.__name__}")
    # Helper function to convert a list to a linked list
    def to_linked_list(lst):
        dummy = ListNode(0)
        current = dummy
        for value in lst:
            current.next = ListNode(value)
            current = current.next
        return dummy.next

    # Helper function to convert a linked list to a list
    def to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    # Test cases
    case_1_list1 = to_linked_list([1, 2, 4])
    case_1_list2 = to_linked_list([1, 3, 4])
    case_2_list1 = to_linked_list([])
    case_2_list2 = to_linked_list([])
    case_3_list1 = to_linked_list([])
    case_3_list2 = to_linked_list([0])

    # Assertions
    assert to_list(mergeTwoLists(case_1_list1, case_1_list2)) == [1, 1, 2, 3, 4, 4], "Test case 1 failed"
    assert to_list(mergeTwoLists(case_2_list1, case_2_list2)) == [], "Test case 2 failed"
    assert to_list(mergeTwoLists(case_3_list1, case_3_list2)) == [0], "Test case 3 failed"

    print("All test cases passed!")

def mergeTwoLists(list1:[ListNode], list2:[ListNode]):
    current = head = ListNode(0) # set up dummy node and current
    while list1 and list2: # loop while both lists are not empty
        if list1.val < list2.val: # list1 is smaller, append the current node of list 1
            current.next = list1
            list1 = list1.next
        else: # list2 is smaller, append the current node of list 2
            current.next = list2
            list2 = list2.next
        current = current.next # move the current node forward as to not override
    # append whichever(if any) list still has values
    if list1:
        current.next = list1
    else:
        current.next = list2
    return head.next

testMergeTwoLists(mergeTwoLists)