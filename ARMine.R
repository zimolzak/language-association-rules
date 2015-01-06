library(arules);

langs <- read.transactions("~/Desktop/code2014-assoc-rule/transactions.txt", format = "basket", sep = "\t", rm.duplicates = TRUE);

lang_rules <- apriori(langs, parameter=list(support = .001, confidence = 0.2));

# inspect(head(sort(lang_rules, by = "confidence"), n = 30)) # too many conf = 1
inspect(head(sort(lang_rules, by = "support"), n = 30))
# inspect(head(sort(lang_rules, by = "support"), n = 30)) # not general

# quality(lang_rules) <- cbind(quality(lang_rules), interestMeasure(lang_rules, method=c("chiSquare", "conviction", "cosine", "coverage", "doc", "gini", "hyperLift", "hyperConfidence", "fishersExactTest", "improvement", "leverage", "lift", "oddsRatio", "phi", "RLD"), langs))

####

require(ggplot2)
liberal <- apriori(langs, parameter=list(support = .0001, confidence = 0))
qplot(support, confidence, data=quality(liberal)) # it takes about 10 sec

detuned <- apriori(langs, parameter=list(support = 0.05, confidence = 0.125))

quality(detuned) <- cbind(quality(detuned), interestMeasure(detuned, method=c("chiSquare", "conviction", "lift", "cosine", "gini", "fishersExactTest", "oddsRatio"), langs))
inspect(head(sort(detuned, by = "support"), n = 30))
inspect(head(sort(detuned, by = "confidence"), n = 30))
inspect(head(sort(detuned, by = "chiSquared"), n = 30))
inspect(head(sort(detuned, by = "conviction"), n = 30))
inspect(head(sort(detuned, by = "lift"), n = 30)) 
inspect(head(sort(detuned, by = "cosine"), n = 30))
inspect(head(sort(detuned, by = "gini"), n = 30))
inspect(head(sort(detuned, decreasing=FALSE, by = "fishersExactTest"), n = 30))
inspect(head(sort(detuned, by = "oddsRatio"), n = 30)) 
