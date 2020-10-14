'''Given input of array of string in format < employee name > : < employee number > separated by comas. 
Employee name should contain only alphabets and employee number should contain only number.
You have to generate password. For example, you give input
Robert:36787,Tina:68721,Jo:56389
Output: tiX
Condition: Length of robert is 6 and 6 is present in employee number of robert(36787), 
so return the alphabet at position 6 that is t.
Now, length of Tina is 4 and 4 is not present in 68721, 
so select the number which is maximum and less than length of Tina so select 2, 
return the alphabet that is at position 2, return i.
Now length of Jo is 2 and it is not in 56389, and there is not any number which is less than 2, so return "X".'''

list = input().split(",")
out = ""
for i in list:
    temp = i.split(":")
    name = temp[0]
    number = temp[1]
    l = len(name)
    max = 0
    for j in number:
        if int(j) <= l:
            if max < int(j):
                max = int(j)
    if max == 0:
        out += "X"
    else:
        out += name[max - 1]
print(out)
