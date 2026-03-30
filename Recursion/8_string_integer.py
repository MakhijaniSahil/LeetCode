class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip() #Remove leading/trailing whitespace
        
        if not s:
            return 0
        
        num = ""
        sign = True # True for positive, False for negative
        
        if s[0] in ["+","-"]:
            if s[0]=="-":
                sign = False
            s = s[1:]
     
        for c in s:
            if not c.isdigit(): #Parse digits until non-digit
                break          
            num+=c  
            
        if not num:
            return 0 #Return 0 if no digits found
        
        num = int(num)
        if not sign:
            num = -num
        
        # Clamp the value to 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if num > INT_MAX:
            return INT_MAX
        if num < INT_MIN:
            return INT_MIN
        
        return num