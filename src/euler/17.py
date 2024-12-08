def get_english_number_representation(n: int) -> str:
    representations = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }

    if n in representations:
        return representations[n]
    if n == 1000:
        return "one thousand"
    numberstring = ""
    if n >= 100:
        hundreds_part = n // 100
        numberstring += f"{representations[hundreds_part]} hundred"
        if n % 100 == 0:
            return numberstring
        else:
            numberstring += " and "
            n -= hundreds_part * 100
    
    if n in representations:
        return numberstring + representations[n]
    else:
        tens_part = n // 10
        numberstring += f"{representations[tens_part * 10]}"
        if n % 10 == 0:
            return numberstring
        else:
            numberstring += "-"
            n -= tens_part * 10
    
    assert n < 10
    return numberstring + representations[n]

def count_letters_in_string(s: str) -> int:
    return len([letter for letter in s if letter != " " and letter != "-"])

assert(count_letters_in_string(get_english_number_representation(342)) == 23)
assert(count_letters_in_string(get_english_number_representation(115)) == 20)
num_letters = 0
for i in range(1, 1001):
    num_letters += count_letters_in_string(get_english_number_representation(i))

print(num_letters)