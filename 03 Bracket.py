def bracketCheck(ip):

    opening = set("[{(")  # Creates an opening paren Set
    stack = []
    count = 0
    for s in ip:
        if s in opening:
            stack.append(s)  # Adds Opening bracket in stack
            count += 1
            continue
        if len(stack) == 0:
            return count + 1
        last = stack.pop()  # Pops last opened bracket to last
        # Checks for closing bracket
        if s == ")" and last == "(":
            count += 1
        elif s == "]" and last == "[":
            count += 1
        elif s == "}" and last == "{":
            count += 1
        else:
            return count + 1  # If not macthed returns the count
    if len(stack) == 0:  # If every bracket is macthed
        return 0  # Then return 0
    else:
        return (
            count + 1
        )  # Else return last count as there is opening bracket left to be closed


n = input()
print(bracketCheck(n))
"""
ip-> ()()(([{}]))
op->0
"""

"""
ip-> ())
op->3
"""
