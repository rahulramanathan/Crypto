# Input Format
#
# There are 2 lines in the input.
# The first line contains a single positive integer 'n'
# The second line contains 'n' space separated integers, the values of f(1) f(2) ... f(n) respectively.
# Enter your code here. Read input from STDIN. Print output to STDOUT


def unique(list_num):
    dict_num = {key:0 for key in list_num}
    for i in list_num:
        dict_num[i] += 1
    for i in dict_num:
        if dict_num[i] is not 1:
            return False
    return True


n = int(input())
list_num = input().split(' ')
if len(list_num) == n and unique(list_num):
    print('YES')
else:
    print('NO')
