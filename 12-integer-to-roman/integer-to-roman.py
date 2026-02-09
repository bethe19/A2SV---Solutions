class Solution:
    def intToRoman(self, n: int) -> str:
        s = ''
        roman = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        for val, sym in roman:
            while n >= val:
                s += sym
                n -= val
                
        return s

