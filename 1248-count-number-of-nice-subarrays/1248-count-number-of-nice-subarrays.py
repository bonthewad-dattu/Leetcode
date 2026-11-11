class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        odd = 0
        freq = {0: 1}
        for num in nums:
            if num % 2 != 0:
                odd += 1
            count += freq.get(odd - k, 0)
            freq[odd] = freq.get(odd, 0) + 1
        return count