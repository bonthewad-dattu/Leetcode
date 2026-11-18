class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        d = dict()
        st = []
        res = [-1] * len(nums1)
        for i in range(len(nums2)):
            while len(st)!=0 and nums2[i] > st[-1]:
                d[st[-1]] = nums2[i]
                st.pop()
            st.append(nums2[i])
        for i in range(len(nums1)):
            if(nums1[i] in d):
                res[i] = d[nums1[i]]      
        return res          

