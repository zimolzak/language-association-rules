Associations in #code2014
========================

Suppose a programmer uses language X. What does that say about whether
the same person uses language Y?

There is a Twitter survey going on, using #code2014. See
http://www.code2014.com/

I decided to use the tweets in response to that survey as a data set.
Right now to get the data in, I do something monstrously ugly.
Process: go to Twitter, search for the hashtag, hit "end" a bunch of
times so it loads more tweets, and copy-paste the resulting long Web
page out of the browser window and into a plain text file called
`output.txt`. Obviously I wanted to do this fast (read: 1 hour) and
not right.

Usage:

    ./analyze.py dump.txt > output.txt

To do
----

# For data import, use a package that actually uses the Twitter API.
Such as: https://github.com/sixohsix/twitter

# For analysis, use an actual association rules package. Such as:
http://www.cs.umb.edu/~laur/ARMiner/ or
http://cran.r-project.org/web/packages/arules/index.html

# Heat map, obvs.
