import unittest
from palindrome import *


class TestSum(unittest.TestCase):

   def test_palindrome(self):
      assert isPalindrome('abcdcba') == True, "Should be True"
      assert isPalindrome('hatdog') == False, "Should be False"
      assert isPalindrome('nurses run') == True, "Should be True"
      assert isPalindrome('123454321') == True, "Should be True"
      assert isPalindrome('nurses-run') == False, "Should be False"
   def test_longPalindrome(self):
      assert isLongestPalindrome('abaxyzzyxf') == 'xyzzyx', "Should be xyzzyx"
      assert isLongestPalindrome('abbaddabsa') == 'baddab', "Should be baddab"
      assert isLongestPalindrome('nurses run') == 'nursesrun', "Should be nurses run"
   def test_minimumCutPal(self):
      assert isMinimumCut('noonabbad') == 2, "Should be 2"
      assert isMinimumCut('nurses run') == 0, "Should be 0"
      assert isMinimumCut('abcde') == 4, "Should be 4"

if __name__ == '__main__':
    unittest.main()