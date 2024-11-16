"""Question 3.41 (Algorithm Design Manual)
You are given a search string and a magazine. You seek to generate all the
characters in the search string by cutting them out from the magazine. Give an
algorithm to efficiently determine whether the magazine contains all the letters
in the search string
"""

from collections import Counter


def can_generate_search_string(search_string, magazine):
    search_count = Counter(search_string)
    magazine_count = Counter(magazine)

    for char, count in search_count.items():
        if magazine_count[char] < count:
            return False
    return True


if __name__ == "__main__":
    print(can_generate_search_string("abc", "abcdefg"))
