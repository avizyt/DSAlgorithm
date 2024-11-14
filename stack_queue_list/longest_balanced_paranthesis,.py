# longest balanced parenthesis


def longest_balanced_parenthesis(string):
    stack = []
    count = 0
    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                continue
            stack.pop()
            count += 2

    return count


if __name__ == "__main__":
    string = ")()(())()()))())))("
    print(longest_balanced_parenthesis(string))
