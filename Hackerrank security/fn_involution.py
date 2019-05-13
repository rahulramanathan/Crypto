# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
list_num = input().split(' ') #ith pos = f(i) i starts from 1
list_num = [int(i) for i in list_num]
if len(list_num) == n:
    #bijective
    f = {i+1: list_num[i] for i in range(n)}
    f_inv = {f[i]: i for i in f.keys()}
    flag = True
    for i in range(1,n+1):
        if f[i] != f_inv[i]:
            flag = False
            break
    if flag :
        print('YES')
    else :
        print('NO')
else:
    #not bijective
    pass