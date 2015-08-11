

def no_duplicates(s):
    l = []
    chars = list(s)
    for ch in chars:
        if ch not in l:
            l.append(ch)
        else:
            return False
    return True

def no_duplicates_no_extra_struc(s):
    chars = list(s)
    for ch in chars:
        if chars.count(ch) > 1:
            return False
    return True

if __name__ == '__main__':

    print no_duplicates_no_extra_struc('abc')
    print no_duplicates_no_extra_struc('aac')
    print no_duplicates_no_extra_struc('aac ')
      

