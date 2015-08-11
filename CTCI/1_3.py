"""
Question 1.3: given two strins, write a method to 
decide if one is a permutation of the other.
"""


def is_perm(str1, str2):
    str1 = list(str1)
    str2 = list(str2)

    if len(str1) != len(str2):
        return False

    for ch in str1:
        if ch not in str2:
            return False
        if str1.count(ch) != str2.count(ch):
            return False
    return True


if __name__ == "__main__":

    print is_perm("abc", "bca")
    print is_perm("asd", "abc")
    print is_perm("abcd", "asdfff")
    print is_perm("amor", "roam")
