class Solution_Brute(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''Brute Force'''
        n = len(nums)
        sorted_nums = sorted(nums) # sort nums - O(nlogn)
        count = 0 # count number of times arrays match
        for x in range(n): # loop for x
            for j in range(n): # loop for each element
                if(sorted_nums[j]!=nums[(x+j)%n]): # if order breaks i.e no rotation for that x
                    break
                if(j==n-1): # if end of array that means we have a rotation for that x
                    count+=1
            if(count>0): # if even one rotation is found then we can return true
                return True
        
        return False # if no rotation return false
    
class Solution_Optimal(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''Optimal'''
        n=len(nums)
        count=0 # count number of times order breaks
        for i in range(n-1): # loop till n-1 to compare with next element
            if(nums[i]>nums[i+1]): # if order breaks then increment count
                count+=1
        
        if(nums[n-1]>nums[0]): # if last element greater than first element then order breaks
            count+=1
        
        if(count>=2): # if order breaks more than once then no sorted rotated array possibnle
            return False
        else:
            return True