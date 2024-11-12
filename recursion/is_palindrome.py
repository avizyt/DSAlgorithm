import re

def is_palindrome(s):
    s = re.sub(r'\W', '', s.lower())
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

line = "A man, a plan, a canal: Panama"

print(is_palindrome(line))
