#!/usr/bin/python3

def to_lower(s):
    if s == None:
        raise TypeError
    s_lower = ""
    
    for i in range(len(s)):
        ascii_val = ord(s[i])
        if ascii_val in range(65, 91):
            s_lower += chr(ascii_val + 32)
        else:
            s_lower += s[i]
    return s_lower

print(to_lower("HeLLo WoRlD"))

