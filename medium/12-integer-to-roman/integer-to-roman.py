class Solution:
    def intToRoman(self, num: int) -> str:
        result  = ''
        num_map = {
            1000: "M", 900: "CM",
            500: "D",  400: "CD",
            100: "C",  90: "XC",
            50: "L",   40: "XL",
            10: "X",   9: "IX",
            5: "V",    4: "IV",
            1: "I"
        }
      
        for key in num_map:
            while num >= key:
                times = num / key
                addition = num_map[key] * int(times)
                result += addition
                num = num % key

        return result