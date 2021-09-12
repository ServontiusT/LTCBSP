passwd = input()

upper_char = False
upper_char_count = 0
lower_char = False
lower_char_count = 0
number_char = False
number_char_count = 0
passwd_valid = 'Invalid'

if (len(passwd) >= 8) and (len(passwd) <= 12):
    for i in passwd:
        if i.isupper():
            upper_char_count = upper_char_count + 1
            if upper_char_count >= 2:
                upper_char = True
        if i.islower():
            lower_char_count = lower_char_count + 1
            if lower_char_count >= 3:
                lower_char = True
        if i.isnumeric():
            number_char_count = number_char_count + 1
            if number_char_count >= 1:
                number_char = True
if upper_char == True and lower_char == True and number_char == True:
    passwd_valid = 'Valid'

print(passwd_valid)