#!/usr/bin/env python
import sys
for arg in sys.argv:
    f = open(arg, 'r')
i = 0



for line in f:
    if '#code2014' in line:
        print line,
        i += 1
    if i > 10:
        quit()

