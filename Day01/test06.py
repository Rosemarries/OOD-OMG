roman_dict = {
    'I': 1, 
    'V': 5,
    'X': 10, 
    'L': 50,
    'C': 100, 
    'D': 500,
    'M': 1000
}

class translator:

    def deciToRoman(self, num):
        roman = ""
        while num//1000 != 0:
            roman += 'M'
            num -= 1000
        if(num >= 900):
            roman += 'CM'
            num -= 900
        while(num//500 > 0):
            roman += 'D'
            num -= 500
        if(num >= 400):
            roman += 'CD'
            num -= 400
        while(num//100 > 0):
            roman += 'C'
            num -= 100
        if(num >= 90):
            roman += 'XC'
            num -= 90
        while(num//50 > 0):
            roman += 'L'
            num -= 50
        if(num >= 40):
            roman += 'XL'
            num -= 40
        while(num//10 > 0):
            roman += 'X'
            num -= 10
        if(num >= 9):
            roman += 'IX'
            num -= 9
        while(num//5 > 0):
            roman += 'V'
            num -= 5
        if(num >= 4):
            roman += 'IV'
            num -= 4
        while(num > 0):
            roman += 'I'
            num -= 1
        return roman

    def romanToDeci(self, s):
        roman_back = list(reversed(list(s)))
        sum = 0
        
        right = roman_dict[roman_back[0]]  
        for numeral in roman_back:
            left = roman_dict[numeral]
            if left < right:
                sum -= left
            else:
                sum += left
            right = left
        return sum

num = int(input("Enter number to translate : "))
print(translator().deciToRoman(num))
print(translator().romanToDeci(translator().deciToRoman(num)))