'''
You are provided two or more strings, 
where each string is associated with the number (seperated by :).
If sum of square of digits is even then rotate the string right by one position,
and if sum of square of digits is odd then rotate the string left by two position.
Input :
Accept multiple values in the form of String:Integer seperated by ‘,’
Output :
Rotated Strings.
Sample Testcases :
I/P 1 :
abcde:234,pqrs:246
O/P 1 :
cdeab
spqr
Explanation : 
For first teststring, ‘abcde’ associated integer is 234, 
squaring 4+9+16=29, which is odd, so we rotate string left by two positions. 
For second teststring, ‘spqr’ associated integer is 246, 
squaring 4+16+36=56, which is even, so we rotate string right by one position.
'''
lst = input().split(",")
for i in lst:
    temp = i.split(":")
    string = temp[0]
    number = temp[1]
    sum = 0
    for n in number:
        sum += int(n)**2
    if sum % 2 == 0:
        print(string[-1], end="")
        print(string[:-1])
    else:
        print(string[2:], end="")
        print(string[:2])
