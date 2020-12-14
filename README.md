Coding Challenge
   * Check Palindrome
   * Longest Palindrome
   * Minimum Cuts Palindrome

Approach:
   * Check Palindrome - compare the reversed string to the input string. If true, string is palindrome.
      <br /> Time Complexity O(n)
   * Longest Palindrome - get all possible palindromes in a string starting from 2 letters.
      <br /> Example of a 7 letter string:
         <br /> 01 012 0123 01234 012345 0123456 01234567
         <br /> 12 123 1234 12345 123456 1234567
         <br /> 23 234 2345 23456 234567
         <br /> 34 345 3456 34567
         <br /> 45 456 4567
         <br /> 56 567
         <br /> 67
      <br /> The last palindrome that will be checked will be the longest.
      <br /> Time Complexity O(n^2)
   * Minimum Cuts Palindrome - used naive recursion algorithm to get the minimum cuts. 
      <br /> Time Complexity O(n)

How to Run:
   * Check Palindrome - python -c "import palindrome; print(palindrome.isPalindrome([inputString]))"
   * Longest Palindrome - python -c "import palindrome; print(palindrome.isLongestPalindrome([inputString]))"
   * Minimum Cuts Palindrome python -c "import palindrome; print(palindrome.isMinimumCut([inputString]))"   