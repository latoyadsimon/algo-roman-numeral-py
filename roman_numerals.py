roman_numeral_to_arabic = {
    'I' : 1,
    'IV': 4,
    'V' : 5,
    'IX': 9,
    'X' : 10,
    'XL': 40,
    'L' : 50,
    'C' : 100,
    'CD': 400,
    'D' : 500,
    'CM' : 900,
    'M' : 1000
}

roman_numeral_priority_order = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
roman_numeral_priority_order_not_lazy = ['M','CM', 'D', 'CD', 'C', 'L', 'XL', 'X', 'V', 'IV', 'I']


def to_roman_common(num, arr):
    output = "";
 
    for numeral in arr:
       
        #  division = num / roman_numeral_to_arabic[numeral]
         floored = num // roman_numeral_to_arabic[numeral]
        #  print(num, "/", roman_numeral_to_arabic[numeral], " = ", division)
        #  console.log(floored)
         if floored > 0:
            # console.log("this is the numeral", numeral)
            # output+= numeral.repeat(floored)
            output+= numeral * floored
            num -= floored * roman_numeral_to_arabic[numeral]
            # if the number is 4, add IV to output
         
    
    print(output)
    return output


def to_roman(num): 
    return to_roman_common(num, roman_numeral_priority_order_not_lazy)

def to_roman_lazy(num): 
    return to_roman_common(num, roman_numeral_priority_order)


# module.exports = { to_roman, to_roman_lazy };

#to_roman_lazy(4); #'IIII'
#to_roman_lazy(150); #'CL'
to_roman_lazy(944); #'DCCCCXXXXIIII'

#to_roman(4); #'IV'
#to_roman(150); #'CL'
to_roman(944); #'CMXLIV'


