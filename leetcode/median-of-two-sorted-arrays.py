# Problem URL:
# https://leetcode.com/problems/median-of-two-sorted-arrays

from functools import lru_cache
class Solution():
    @lru_cache(None)
    def findNthNumber(self,n,nums1_start,nums2_start):
        # print(n,nums1,nums2)
        # nums1 = self.nums1[nums1_start:]
        # nums2 = self.nums2[nums2_start:]
        if nums1_start == self.nums1_len:
            return self.nums2[n+nums2_start]
        if nums2_start == self.nums2_len:
            return self.nums1[n+nums1_start]
        if n == 0:
            return min(self.nums1[nums1_start],self.nums2[nums2_start])
        
        sub = (n-1)//2
        
        a1 = min(self.nums1_len - nums1_start -1, sub )
        a2 = min(self.nums2_len - nums2_start -1, sub )

        if self.nums1[nums1_start + a1] < self.nums2[nums2_start +a2]:
            #logic
            res = self.findNthNumber(n - a1 - 1,nums1_start + a1+1,nums2_start)
        else:
            #logic
            res = self.findNthNumber(n - a2 - 1,nums1_start,nums2_start +a2+1)


        #res  = 0
        return res
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        self.nums1 = nums1
        self.nums1_len = len(nums1)
        self.nums2 = nums2
        self.nums2_len = len(nums2)

        r = self.nums2_len + self.nums1_len
        if r % 2 ==0:
            a = self.findNthNumber(r//2 - 1,0,0)
            b = self.findNthNumber(r//2,0,0)
            #print(a,b)
            return (a + b)/2.0
        else:
            a = self.findNthNumber(r//2,0,0)
            return a
