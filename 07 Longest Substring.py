string = input()
length = len(string)
unique = ""
for i in range(length):
    substring = string[i]
    for j in range(i + 1, length):
        substring += string[j]
        sub_len = len(substring)
        if sub_len >= 3 and len(set(substring)) == sub_len:
            if len(unique) < sub_len:
                unique = substring
if len(unique) == 0:
    print(-1)
else:
    print(unique)
