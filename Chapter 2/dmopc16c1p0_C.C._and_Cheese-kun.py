#dmopc16c1p0_C.C._and_Cheese-kun

za_width = int(input())
cheese_percent = int(input())

if za_width == 3 and cheese_percent >= 95:
    print('C.C. is absolutely satisfied with her pizza.')
elif za_width == 1 and cheese_percent <= 50:
    print('C.C. is fairly satisfied with her pizza.')
else:
    print('C.C. is very satisfied with her pizza.')