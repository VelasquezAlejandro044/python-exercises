# 1a is_vowel
def is_vowel(x):
    return x in "aeiouAEIOU"

# 1b calculate_tip
def calculate_tip(tip_percentage, bill_total):
    if tip_percentage > 0 and tip_percentage < 1:
        return tip_percentage * bill_total
    else:
        return "Can't work under this conditions"

# 1c get_letter_grade
def get_letter_grade(num):
    if num >= 88:
        return "A"
    elif num >= 80:
        return "B"
    elif num >= 67:
        return "C"
    elif num >= 66:
        return "D"
    else:
        return "F"
