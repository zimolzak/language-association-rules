#!/usr/bin/env python
# usage: ./analyze.py dump.txt 
import sys
import re
for arg in sys.argv:
    if 'txt' in arg:
        f = open(arg, 'r')

Languages = ['javascript', 'python', 'java', 'ruby', 'sql', 'bash', \
                 'php', 'c#', 'c', 'c++', 'go', 'clojure', 'haskell',\
                 'scala', 'objective-c', 'swift', 'delphi', 'f#',\
                 'coffeescript', 'erlang', 'rust', 'r', 'groovy', 'lua',\
                 'perl']
Languages.sort()

# create triangular matrix filled with 0s.
matrix = dict()
row_num = 0
for row in Languages:
    new_row = dict()
    for col in Languages[row_num+1:]:
        new_row[col] = 0
    matrix[row] = new_row
    row_num += 1

# populate matrix with counts of language pairs
for line in f:
    languages_mentioned = []
    if not '#code2014' in line:
        continue
    row_num = 0
    words = re.split('[\s,.]', line.lower())
    for lang1 in Languages:
        if lang1 in words:
            for lang2 in Languages[row_num+1:]:
                if lang2 in words:
                    pair = [lang1, lang2]
                    pair.sort()
                    matrix[pair[0]][pair[1]] += 1
        row_num += 1

# print matrix
rownames = matrix.keys()
rownames.sort()
for label in rownames:
    print label[0:6], "\t",
print "\n",
row_num = 0
for i in rownames:
    row_num += 1
    print ("\t" * row_num),
    colnames = matrix[i].keys()
    colnames.sort()
    for j in colnames:
        print matrix[i][j], "\t",
    print i[0:6]

## NEXT STEP, get it into R and use library(arules) !!
