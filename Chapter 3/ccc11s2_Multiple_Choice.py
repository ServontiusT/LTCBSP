n = int(input())
n2 = n * 2

total_correct = 0
answer_given = ''

for num in range(n2):
    answer_given = answer_given + str(input())
for num2 in range(n):
    if answer_given[num2] == answer_given[num2 - n]:
        total_correct = total_correct + 1

print(total_correct)