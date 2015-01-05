Associations in #code2014
========================

Suppose a programmer uses language X. What does that say about whether
the same person uses language Y?

Hypotheses
----

I bet the functional languages group together rather than avoiding
each other. That is, if you used one functional language in 2014, I
bet you used some other functional ones too; as opposed to using one
functional language, getting locked into it, and avoiding other
functional languages.

Rough conclusions
----

I think I see an association between Clojure and Scala. Maybe not the
other functional ones? Bash, C, and SQL seem to go together like
peanut butter, jelly, and bread. C and JavaScript look like they might
avoid each other. Swift and Objective-C look like they are friends,
which makes a heck of a lot of sense.

Methods
----

There is a Twitter survey going on, using #code2014. See
http://www.code2014.com/

I decided to use the tweets in response to that survey as a data set.
Right now to get the data in, I do something monstrously ugly.
Process: go to Twitter, search for the hashtag, hit "end" a bunch of
times so it loads more tweets, and copy-paste the resulting long Web
page out of the browser window and into a plain text file called
`output.txt`. Obviously I wanted to do this fast (read: 1 hour) and
not right. These people are doing it right:
https://github.com/hybridgroup/hashcode

Usage:

    ./analyze.py dump.txt > output.txt

So far it just outputs the counts of how many times two items
(languages) co-occur in the same "market basket" (survey respondent in
2014). No real association rule mining (confidence, support, cosine,
etc.)

To do
----

* For data import, use a package that actually uses the Twitter API.
Such as: https://github.com/sixohsix/twitter

* For analysis, use an actual association rules package. Such as:
http://www.cs.umb.edu/~laur/ARMiner/ or
http://cran.r-project.org/web/packages/arules/index.html See
www.cse.msu.edu/~ptan/papers/IS.pdf for more on association rules.

* Heat map, obvs.
