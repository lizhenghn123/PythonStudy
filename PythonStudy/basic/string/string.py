#!/usr/bin/env python
#coding=utf-8
import string

def test_string():
    s1 = "hello world"
    print(s1)
    print(s1[0], s1[2:8])

    s1 = s1[:6] + "python"
    print(s1)

    print(string.letters, string.digits)

    s1 += string.digits
    print(s1)

    #s2 = '_'.join((s1[0], s1[1], s1[2-6], "fff3f", 1))
    s2 = '_'.join(("dfdfgdf", s1[1], s1[2], "fff3f", "1"))
    print(s2)

    s2 = "WHAT IS YOUR NAME?"
    s2.lower()

    print(s2.count("A"))
    print(s2.endswith("ME?"));
    print(s2.startswith("what"))
    
    print(s2.find("S Y"))

# end

if __name__ == "__main__":
    test_string()