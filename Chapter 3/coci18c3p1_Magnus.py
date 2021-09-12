given_string = input()

honi_chars = ''

for char in given_string:
    if (char != 'H') and (char != 'O') and (char != 'N') and (char != 'I'):
        given_string.replace(char, '')
    else:
        honi_chars = honi_chars + char



print(honi_chars)