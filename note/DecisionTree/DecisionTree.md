# Decision Tree

## What is Decision Tree

  First, let's see the definition of decision tree on [Wiki]( https://en.wikipedia.org/wiki/Decision_tree ).

> A **decision tree** is a [decision support](https://en.wikipedia.org/wiki/Decision_support_system) tool that uses a [tree-like](https://en.wikipedia.org/wiki/Tree_(graph_theory)) [model](https://en.wikipedia.org/wiki/Causal_model) of decisions and their possible consequences, including [chance](https://en.wikipedia.org/wiki/Probability) event outcomes, resource costs, and [utility](https://en.wikipedia.org/wiki/Utility). It is one way to display an [algorithm](https://en.wikipedia.org/wiki/Algorithm) that only contains conditional control statements.
>
> Decision trees are commonly used in [operations research](https://en.wikipedia.org/wiki/Operations_research), specifically in [decision analysis](https://en.wikipedia.org/wiki/Decision_analysis), to help identify a strategy most likely to reach a [goal](https://en.wikipedia.org/wiki/Goal), but are also a popular tool in [machine learning](https://en.wikipedia.org/wiki/Decision_tree_learning).

  Decision tree is a way to do the classification. It works just like human being. For example, when you want to know whether a computer is a good computer, you may first look at the RAM of this computer and then the CPU and then the GPU and so on. If we represent this process with a tree, we may do like this:

<img src=" DTexample.png" alt="An example" style="zoom:67%;" />

  First, we check the RAM of this computer, if it doesn't have large RAM, we think this computer isn't a good computer. If it has large RAM, we continue to check the CPU and so on.

  So, if we can generate a tree like this from a data set, we can let the machine do the classification job based on this tree just like us. This is the basic idea of the decision tree.

## How to create a decision tree