class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        old = x
        New=0
        while x > 0:
         New = New * 10+x%10
         x = x//10
        return New == old
print(Solution().isPalindrome(567))
print(Solution().isPalindrome(313))
