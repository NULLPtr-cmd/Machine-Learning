# Naive Bayes

Author: Zhang Xiaozheng Date: 2019/10/31

When we do classification, we want to find the class of a given data. From the perspective of probability theory, we want to find the distribution function *P(c|x)*. So we can choose the class which makes it's distribution function max. 

Some algorithm like decision tree or logistic regression just want to find *P(c|x)* directly. But what Bayes Classifier do is using Bayes formula.
$$
P(c|x)=\frac{P(c)P(x|c)}{P(x)}
$$
So our task turns into find *P(c)* and *P(x|c)*.

To find *P(c)* and *P(x|c)*, we need to use MLE(Maximum Likelihood Estimation) to estimate *P(x|c)*. 

But if we directly estimate *P(x|c)*, there will be so many possible combination so it will takes 

