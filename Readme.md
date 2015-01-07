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

Conclusions
----

*By inspection of counts of co-occurrence:* I think I see an
association between Clojure and Scala. Maybe not the other functional
ones? C and JavaScript look like they might avoid each other. Swift
and Objective-C look like they are friends, which makes a heck of a
lot of sense.

*By association rules:* Bash, C, and SQL go together like peanut
butter, jelly, and bread.

Methods
----

There is a Twitter survey going on, using #code2014. I decided to use
the tweets in response to that survey as a data set.

1. Right now to get the data in, I do something monstrously ugly. Go
to Twitter.com, search for the hashtag, hit the keyboard "end" key a
bunch of times so it loads more tweets, and copy-paste the resulting
long Web page out of the browser window and into a plain text file
called `dump.txt`. Obviously I wanted to do this fast (read: 1 hour)
and not right. These people are doing it right:
https://github.com/hybridgroup/hashcode

2. `./count.py dump.txt > output.txt`

3. Inspect `output.txt` which is the counts of how many times two
items (languages) co-occur in the same "market basket" (survey
respondent in 2014). Draw your own conclusions from squinting at the
data.

4. `./item_sets.py dump.txt > transactions.txt`

5. Use R to run `ARMine.R`

To do
----

* For data import, use a package that actually uses the Twitter API.
Such as: https://github.com/sixohsix/twitter

* Heat map, obvs.

References
----
* http://www.cs.umb.edu/~laur/ARMiner/
* http://cran.r-project.org/web/packages/arules/index.html
* www.cse.msu.edu/~ptan/papers/IS.pdf
* http://www.code2014.com/
