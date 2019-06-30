n = 3
list_num = (2, 3, 1)
f = {i+1: list_num[i] for i in range(n)}
f_f = {i: f[f[i]] for i in f.keys()}
print(f_f)
print('Hello')
