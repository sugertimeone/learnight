# _*_ coding: utf-8 _*_
def trim(s):
    print(s)
    if s != '':
        while s[0] == ' ':
            if s == ' ':
                s = ''
                return s
            if s != '':
                s = s[1:]
        while s[-1] == ' ':
            s = s[:-1]
    return s