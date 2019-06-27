# Enter your code here. Read input from STDIN. Print output to STDOUT
def trans(key, msg):
    keyword = "".join(sorted(set(key), key=key.index()))


n = int(input())
keywords = []
messages = []
for i in range(n):
    keywords.append(input())
    messages.append(input())
for i in range(n):
    print(trans(key=keywords[i]),msg=messages[i])
