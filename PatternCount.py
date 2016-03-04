__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com, fb.com/aliyyousuf'

# Codes provided by course

# Implementation of pattern count.


def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count


#Pattern = "CGCG"
#text = "CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC"

#print(PatternCount(Pattern,text))
