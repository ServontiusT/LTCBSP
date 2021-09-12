# 𝐴-minor is defined as (𝐴(tonic),𝐵,𝐶,𝐷(subdominate),𝐸(dominate),𝐹,𝐺)
# 𝐶-major is defined as (𝐶(tonic),𝐷,𝐸,𝐹(subdominate),𝐺(dominate),𝐴,𝐵)
# Sample Input CD|EC|CD|EC|EF|G|EF|G|GAGF|EC|GAGF|EC|CG|C|CG|C

composition_given = str(input())

c_major_count = 0
a_minor_count = 0

for i in range(len(composition_given)):
    if (i == 0) or (composition_given[i - 1] == '|'):
        if composition_given[i] == 'A' or composition_given[i] == 'D' or composition_given[i] == 'E':
            a_minor_count = a_minor_count + 1
        if composition_given[i] == 'C' or composition_given[i] == 'F' or composition_given[i] == 'G':
            c_major_count = c_major_count + 1

if (c_major_count) == (a_minor_count):
    if composition_given[-1] == 'C':
        c_major_count = c_major_count + 1
    elif composition_given[-1] == 'A':
        a_minor_count = a_minor_count + 1

if (c_major_count) > (a_minor_count):
    print('C-dur')
else:
    print('A-mol')
