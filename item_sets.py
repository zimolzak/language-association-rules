#!/usr/bin/env python
# usage: ./analyze.py dump.txt > transactions.txt
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

for line in f:
    if not '#code2014' in line:
        continue
    words = re.split('[\s,.]', line.lower())
    market_basket = []
    for this_language in Languages:
        if this_language in words:
            market_basket.append(this_language)
    print "\t".join(market_basket)
