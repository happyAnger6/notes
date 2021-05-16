def roman_to_int(s):
    num, n = 0, len(s)
    one_roma = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    two_roma = dict(IV=4, IX=9, XL=40, XC=90, CD=400, CM=900)
    
    i = 0
    while i < n:
        one_char = s[i]
        two_char = s[i:i+2] if i < n - 1 else None

        if two_char and two_char in two_roma:
            num += two_roma[two_char]
            i += 2
        else:
            num += one_roma[one_char]
            i += 1
    return num

if __name__ == "__main__":
    print(roman_to_int("III"))
    print(roman_to_int("IV"))
    print(roman_to_int("IVV"))
    print(roman_to_int("IX"))
    print(roman_to_int("IXX"))
    print(roman_to_int("LVIII"))

        
            
                




        
            
                



