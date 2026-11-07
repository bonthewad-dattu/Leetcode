class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        product=1
        result=[]
        zero_count=0
        for i in range(0,len(nums)):
            if nums[i]!=0:
              product=product*nums[i]
            else:
                zero_count=zero_count+1 
        if zero_count==1:
            for j in nums:
                if j!=0:
                    result.append(0)
                else:
                    result.append(product)
            return result
        elif(zero_count>1):
            for j in nums:
                result.append(0)
            return result
        else:
            for i in nums:
                result.append(product//i)
            return result