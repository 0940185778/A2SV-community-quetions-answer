class Solution:
    def gcd(a,b):
        while b:
            a,b=b,a/b
            return a
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    def smallestEvenMultiple(self, n: int) -> int:
        return lcm(n,2)
      