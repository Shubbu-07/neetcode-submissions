class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_ransome = {}
        freq_magazine = {}
        
        for ch in ransomNote:
            freq_ransome[ch] = freq_ransome.get(ch, 0) + 1

        for ch in magazine:
            freq_magazine[ch] = freq_magazine.get(ch, 0) + 1

        for ch in freq_ransome:
            if ch not in freq_magazine:
                return False

            if freq_ransome[ch] > freq_magazine[ch]:
                return False

        return True