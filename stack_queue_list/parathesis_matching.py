# Matching paranthesis
def parathesis_matching(string):
    """
    Checks if the parentheses in a given string are balanced.

    This function uses a stack to track opening parentheses '(' and
    ensures that each closing parenthesis ')' has a corresponding
    opening parenthesis. It returns True if the parentheses are
    balanced, otherwise returns False.

    Args:
        string (str): The input string containing parentheses to be checked.

    Returns:
        bool: True if parentheses are balanced, False otherwise.
    """
    stack = []
    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


if __name__ == "__main__":
    string = "((())())()()"
    print(parathesis_matching(string))
