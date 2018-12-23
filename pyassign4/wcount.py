#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Kuangwenyu"
__pkuid__  = "1800013245"
__email__  = "w.y.kuang@pku.edu.cn"
"""

import string
import sys
from collections import Counter
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    lst1 = lines.split()
    lst2 = []  # 去掉紧跟单词的符号
    for str in lst1:
        word = ''
        for char in str:
            if char not in string.punctuation:
                word += char.lower()
        lst2.append(word)
    t = tuple(lst2)
    ct = Counter(t)
    lst3 = ct.most_common(topn)
    for (word,count) in lst3:
        print(word,'\t\t\t', count)  
    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
        
    try:
        with urlopen(sys.argv[1]) as f:
            doc = f.read().decode()
        if len(sys.argv) == 2:
            wcount(doc)
        else:
            wcount(doc, int(sys.argv[2]))
    except ValueError as err:
        print('Error: Please input an int after url')
    except Exception as err:
        print('Error: {0}'.format(err))
