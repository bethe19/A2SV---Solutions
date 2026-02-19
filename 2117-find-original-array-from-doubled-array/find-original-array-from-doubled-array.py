class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 == 1:
            return []

        cnt = Counter(changed)
        changed.sort()

        ans = []

        for num in changed:
            if cnt[num] == 0:
                continue

            if cnt[2 * num] == 0:
                return []

            cnt[num] -= 1
            cnt[2 * num] -= 1
            ans.append(num)

        return ans
