from utils.function import add

def count_word(s, c):
    assert isinstance(s, str)
    assert isinstance(c, str) & (len(c) == 1)
    num = 0
    for i in range(len(s)):
        if (s[i] == c):
            num = add(num, 1)
    return num
