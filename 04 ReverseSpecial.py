string = input()
arr = []
op = ""
for x in string[::-1]:
    if x.isalnum():
        arr.append(x)
i = 0
for x in string:
    if x.isalnum():
        op += arr[i]
        i += 1
    else:
        op += x
print(op)
