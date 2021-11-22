#ex 3 : 25 minutes

number = int(input("Enter integer number : "))

def convert_integer_to_roman(number):
    """
    The function will convert any integer between 1 and 3999 to a roman numeral 
    using the following roman digits : ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    There is no roman numeral for 0.
    The converstion of any number higher than 3999 with the roman digits used would be inacurate.

    Parameters
    -----------
    number : int : the integer to be converted
    -----------
    """

    digits = {
        "M":1000, 
        "CM":900, 
        "D":500, 
        "CD":400, 
        "C":100, 
        "XC":90,
        "L":50,
        "XL":40, 
        "X":10, 
        "IX":9, 
        "V":5, 
        "IV":4, 
        "I":1
    }

    result = []
   
    original_number = number
   
    if number <1 or number>3999 :
        return "This number can't get converted into roman numeral"
        
    else :
        for roman_digit in digits:

            divider = digits[roman_digit]
            quotient = number // divider

            for repetition in range(quotient) :

                result.append(roman_digit)
                number-=divider
    
        final_result = ''.join(result)

        return str(original_number) + ' becomes ' + str(final_result)

print(convert_integer_to_roman(number))
