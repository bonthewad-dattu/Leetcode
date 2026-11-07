class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        product=1
        l1=[]
        zero_count=0
        for i in range(0,len(nums)):
            if nums[i]!=0:
              product=product*nums[i]
            else:
                zero_count=zero_count+1 
        if zero_count==1:
            for j in nums:
                if j!=0:
                    l1.append(0)
                else:
                    l1.append(product)
            return l1
        elif(zero_count>1):
            for j in nums:
                l1.append(0)
            return l1
        else:
            for i in nums:
                l1.append(product//i)
            return l1