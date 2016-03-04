__author__ = 'Mohammad Yousuf Ali, aliyyousuf@gmail.com, fb.com/aliyyousuf'

# This problem wants us to remove all duplicates from MostFrequentWords ouptut:

# Sample Input:
#      ACGTTGCATGTCGCATGATGCATGAGAGCT

#      4

# Sample Output:
#    CATG GCAT

from MostFrequentWord import FrequentWords

without_duplicate = list(set(FrequentWords(Text,k)))  # set function removes all duplicates.