num_of_iterations = int(input())

s_count = 0
t_count = 0

for i in range(num_of_iterations):
    input_sentence = input()
    for s in range(len(input_sentence)):
        if (input_sentence[s] == 's') or (input_sentence[s] == 'S'):
            s_count = s_count + 1
        if (input_sentence[s] == 't') or (input_sentence[s] == 'T'):
            t_count = t_count + 1

if s_count >= t_count:
    print('French')
else:
    print('English')

'''
The following lines were used during testing.
print('S Count ' + str(s_count))
print('T Count ' + str(t_count))
'''
