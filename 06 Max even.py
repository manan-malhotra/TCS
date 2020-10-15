'''
Find the max even no possible
'''


def large(lst):
    if len(lst) == 0:
        return odd
    if res[-1] % 2 == 0:
        return res
    else:
        for j in range(2, len(lst) + 1):
            if res[-j] % 2 == 0:
                ev = res.pop(-j)
                res.append(ev)
                return res
        else:
            return odd


odd = [-1]
s1 = []
s = str(input())
for i in s:
    if i.isdigit():
        s1.append(int(i))
res = sorted(s1, reverse=True)
out = large(s1)
for i in out:
    print(i, end="")
