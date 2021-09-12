input_string = input()

happy_emoji_count = input_string.count(':-)')
sad_emoji_count = input_string.count(':-(')

if (happy_emoji_count == sad_emoji_count) and (happy_emoji_count > 0) and (sad_emoji_count > 0):
    print('unsure')
elif happy_emoji_count > sad_emoji_count:
    print('happy')
elif happy_emoji_count < sad_emoji_count:
    print('sad')
else:
    print('none')