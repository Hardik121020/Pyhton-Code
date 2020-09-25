
import math
import os
import random
import re
import sys
import collections

def company_logo(string):
    s1 = collections.Counter(string)
    
    sorted_dict = collections.OrderedDict(sorted(s1.items(), key = lambda kv : kv[1], reverse=True))
    print(sorted_dict)
    count = 0
    for i in sorted_dict:
        if count != 3:
            print("{} {}".format(i,sorted_dict[i]))
            count = count + 1
            

if __name__ == '__main__':
    s = raw_input()
    company_logo(s)
