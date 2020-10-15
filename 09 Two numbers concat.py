'''
You are given a list of numbers from 1 to 9,
in which each word is seperated by ‘,’. 
Your job is to find the sum of two numbers. 
These two numbers are needed to be calculated as per following rules : 
1. First number should be calculated as :
Add all the numbers that do not come between  5 and 8 in the input.
2.  Second number should be calculated as :
Append all the numbers to each other that comes between 5 and 8 (inclusive).
Find the sum of both numbers.
Note : 5 always comes before 8.
Number of 5’s = Number of 8’s. 
Input : 
First Input : List of numbers
Output : 
“Sum of both numbers”
Sample Testcases :
I/P 1:
3,4,5,2,7,9,8,3,2
O/P 1:
52810
'''
lst = list(map(int, input().split(",")))
five = lst.index(5)
eight = lst.index(8)
a = sum(lst[:five])
b = sum(lst[eight + 1:])
n1 = a+b
rest = lst[five:eight+1]
n2 = ""
for i in rest:
    n2 += str(i)
print(n1+int(n2))
