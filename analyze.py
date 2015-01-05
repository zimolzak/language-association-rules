#!/usr/bin/env python
# usage: ./analyze.py dump.txt 
import sys
for arg in sys.argv:
    if 'txt' in arg:
        f = open(arg, 'r')

Languages = ['javascript', 'python', 'java', 'ruby', 'sql', 'bash', \
                 'php', 'c#', 'c', 'c++', 'go', 'clojure', 'haskell',\
                 'scala', 'objective-c', 'swift', 'delphi', 'f#',\
                 'coffeescript', 'erlang', 'rust', 'r', 'groovy', 'lua',\
                 'perl']

Languages.sort()

matrix = dict()
row_num = 0
for row in Languages:
    new_row = dict()
    for col in Languages[row_num+1:]:
        new_row[col] = 0
    matrix[row] = new_row
    row_num += 1

for line in f:
    languages_mentioned = []
    if not '#code2014' in line:
        continue
    row_num = 0
    for lang1 in Languages:
        if lang1 in line:
            for lang2 in Languages[row_num+1:]:
                if lang2 in line:
                    pair = [lang1, lang2]
                    pair.sort()
                    matrix[pair[0]][pair[1]] += 1
        row_num += 1

rownames = matrix.keys()
rownames.sort()

print "\t",
for label in rownames:
    print label[0:6], "\t",
print "\n",

for i in rownames:
    colnames = matrix[i].keys()
    colnames.sort()
    print i[0:6], "\t", 
    for j in colnames:
        print matrix[i][j], "\t",
    print "\n",
