def isPalindrome(input):
    # Compare input to reverse input
    inputString = input.replace(" ","")
    return inputString == inputString[::-1]

def isLongestPalindrome(input):
    inputString = input.replace(" ","")
    stringLen = len(inputString)
    # if input string is empty, return 0
    if stringLen <= 0:
        return 0
    longestPal = str('') # handles empty input
    for row in range(1, stringLen):
        for col in range(0, stringLen - row):
            if isPalindrome(inputString[col:row+col]):
                longestPal = inputString[col:row+col]
    return longestPal
 
def minPalPartion(string, firstIndex, stringLen): 
    # if input string is empty or a palindrome, return 0
    if firstIndex >= stringLen or isPalindrome(string[firstIndex:stringLen + 1]): 
        return 0
    ans = float('inf') 
    # Naive recursion algorithm
    for k in range(firstIndex, stringLen): 
        count = (1 + minPalPartion(string, firstIndex, k) + minPalPartion(string, k + 1, stringLen)) 
        if count < ans:
            ans = count
    return ans 

def isMinimumCut(stringInput):
    return minPalPartion(stringInput.replace(" ",""), 0, len(stringInput) - 1)
