class RomanNumeralsConverter:
    def __init__(self):
        self.roman_to_int_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def roman_to_int(self, s: str) -> int:
        total = 0
        length = len(s)

        
        for i in range(length):
            current_value = self.roman_to_int_map[s[i]]
            
            
            if i < length - 1 and self.roman_to_int_map[s[i+1]] > current_value:
                total -= current_value
            else:
                total += current_value

        return total


converter = RomanNumeralsConverter()
print(converter.roman_to_int("MCMXCIV"))  
print(converter.roman_to_int("LVIII"))    
print(converter.roman_to_int("IX"))       
