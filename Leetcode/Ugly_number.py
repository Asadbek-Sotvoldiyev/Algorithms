class Solution(object):
    def isUgly(self, n):
        if n<=0:
            return False
        else:
            while n%2==0:
                n = n/2
            while n%3==0:
                n/=3
            while n%5==0:
                n/=5
        return n==1

num = Solution()
print(num.isUgly(6))
# Result: True
print(num.isUgly(8))
# Result: True
print(num.isUgly(14))
# Result: False
