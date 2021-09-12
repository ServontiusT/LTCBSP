prev_month_mb = int(input())
month_count = int(input())

excess_mb = 0

for i in range(month_count):
    mb_used = int(input())
    excess_mb = excess_mb + prev_month_mb - mb_used

print(prev_month_mb + excess_mb)