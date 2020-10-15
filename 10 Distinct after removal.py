'''
Given an array of items, an ith index element denotes the item id’s, 
and given a number m, the task is to remove m elements such that there 
should be minimum distinct id’s left. Print the number of distinct id’s.
Examples:
Input: arr[] = { 2, 2, 1, 3, 3, 3} m = 3
Output: 1
Explanation:
Remove 1 and both 2’s.
So, only 3 will be left, hence distinct number of element is 1.
Input: arr[] = { 2, 4, 1, 5, 3, 5, 1, 3} m = 2
Output: 3
Explanation:
Remove 2 and 4 completely. 
So, remaining 1, 3 and 5 i.e. 3 elements.
'''
rem = int(input())
list_num = list(map(int, input().split(",")))
list_element_count = []
set_distinct = set(list_num)
for i in set_distinct:
    count = list_num.count(i)
    list_element_count.append(count)
list_element_count.sort()
length = len(list_element_count)
for count in list_element_count:
    if count <= rem:
        rem -= count
        length -= 1
    else:
        break
print(length)
