class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = Counter(chars)
        res = 0
        for word in words:
            wordmap = Counter(word)
            isGood = True
            for i in wordmap:
                if i not in chars or wordmap[i] > chars[i]:
                    isGood = False
                    break
            if isGood: res += len(word)
        
        return res

