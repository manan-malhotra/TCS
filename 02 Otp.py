'''
Input will be given like 4365188
Example : seperate odd place Integers :: 3,5,8
You have to return a 4 digit OTP by squaring the digits.
Digits from above example is 3,5,8
Square of those numbers is 9,25,64
So the otp to be returned is first four digits 9256
'''
n = input()
otp = ""
l = len(n)
for i in range(1, l, 2):
    num = int(n[i]) ** 2
    otp += str(num)
print(otp[:4])
