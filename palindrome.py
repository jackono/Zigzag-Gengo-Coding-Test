def isPalindrome(s):
    return s == s[::-1]

def isLongestPalindrome(s, paliLen):
    if paliLen <= 0:
        return 0
    longestPali = str('')
    for i in range(1, paliLen):
        for j in range(0, paliLen - i):
            if isPalindrome(s[j:i+j]):
                longestPali = s[j:i+j]
    return longestPali
 
def minPalPartion(string, i, j): 
    if isPalindrome(string[i:j + 1]): 
        return 0
    ans = float('inf') 
    for k in range(i, j): 
        count = ( 
            1 + minPalPartion(string, i, k) 
            + minPalPartion(string, k + 1, j) 
        ) 
        ans = min(ans, count) 
    return ans 

s = input("Enter your value: ") 

if isPalindrome(s.replace(" ","")):
    print("True")
else:
    print("False")

print(isLongestPalindrome(s.replace(" ",""), len(s) + 1))
print(minPalPartion(s.replace(" ",""), 0, len(s) - 1)) 