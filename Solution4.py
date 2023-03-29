class Solution(object):
    def helper(self, strs, m, n, i):
        max_so_far = 0
        for idx in range(i, len(strs)):
            zeroes, ones = strs[idx].count('0'), strs[idx].count('1') 
            if m >= zeroes and n >= ones:
                max_so_far = max(max_so_far, self.helper(strs, m-zeroes, n-ones, idx+1)+1)
        return max_so_far
    
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        cache = {}
        return self.helper(strs, m, n, 0)