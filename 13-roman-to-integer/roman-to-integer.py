class Solution(object):
    def romanToInt(self, s):
        roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        value = [1, 5, 10, 50, 100, 500, 1000]
        sum = 0
        for i in range (len(s)):
            if s[i] in roman:
                if i+1 != len(s) and ((s[i] == "I" and (s[i + 1] == 'V' or s[i + 1] == 'X')) or (s[i] == "X" and (s[i + 1] == 'L' or s[i + 1] == 'C')) or (s[i] == "C" and (s[i + 1] == 'D' or s[i + 1] == 'M'))):
                    sum -= value[roman.index(s[i])]
                else:
                    sum += value[roman.index(s[i])]
        return sum

        