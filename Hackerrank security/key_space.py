n = input()
k = int(input())
list_num = [str((int(d)+k) % 10) for d in n]
print("".join(list_num))
