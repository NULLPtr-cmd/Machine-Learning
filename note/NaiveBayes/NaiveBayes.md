# Naive Bayes

Author: Zhang Xiaozheng Date: 2019/10/31

When we do classification, we want to find the class of a given data. From the perspective of probability theory, we want to find the distribution function *P(c|x)*. So we can choose the class which makes it's distribution function max. 

Some algorithm like decision tree or logistic regression just want to find *P(c|x)* directly. But what Bayes Classifier do is using Bayes formula.
$$
P(c|x)=\frac{P(c)P(x|c)}{P(x)}
$$
So our task turns into find *P(c)* and *P(x|c)*.

To find *P(c)* and *P(x|c)*, we need to use MLE(Maximum Likelihood Estimation) to estimate *P(x|c)*. 

But if we directly estimate *P(x|c)*, there will be so many possible combinations so it will takes a long time to calculate. So what Naive Bayes do is to suppose all the features in ***X*** is independent. So we can rewrite our equation.
$$
P(x|c)=\prod_{i=1}^{K}P(x_i|c)
$$
  In this way, we just need to estimate these *K* distribution function separately.

## MLE

 After an observation, we have a data set
$$
X=\{x_1,x_2,...,x_n\}
$$
Suppose we already know the form of its probability density function which is:
$$
f(x;\theta_1,\theta_2,...,\theta_k)
$$
So we define Likelihood Function:
$$
L(\theta_1,\theta_2,...,\theta_k)=\prod_{i=i}^{k}f(x_i;\theta_1,\theta_2,...,\theta_k)
$$
As this data has been observed by us, so we can say that the probability of this kind of sample is quite large. What MLE do is to find a group of *θ* which can make the value of Likelihood Function max.

-------

So after use MLE, for a data set *D*,we can have:
$$

$$
