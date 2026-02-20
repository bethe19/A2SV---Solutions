class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_rn = Counter(list(ransomNote)) 
        counter_m = Counter(list(magazine)) 

        for k,v in counter_rn.items():
            if k not in counter_m or v > counter_m[k]:
                return False
        
        return True