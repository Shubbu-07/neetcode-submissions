class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1 
            else:
                freq[num] = 1

        res = max(freq, key=freq.get)
        return res