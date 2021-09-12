#coci06c5p1_Trik

swaps = input()
ball_loc = 1

for swap in swaps:
    if swap == 'A' and ball_loc == 1:
        ball_loc = 2
    elif swap == 'A' and ball_loc == 2:
        ball_loc = 1
    elif swap == 'B' and ball_loc == 2:
        ball_loc = 3
    elif swap == 'B' and ball_loc == 3:
        ball_loc = 2
    elif swap == 'C' and ball_loc == 1:
        ball_loc = 3
    elif swap == 'C' and ball_loc == 3:
        ball_loc = 1

print(ball_loc)