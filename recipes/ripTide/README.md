![Alt text](https://github.com/labyrinthinesecurity/automatedReasoning/blob/main/recipes/ripTide/monsterRipTide.png)

**ripTide** is an automated reasoning pattern which checks whether a principal Id belongs to an exceptions list.

- Suppose that, from ground truth, we collect a list of principal IDs belonging to a first set. Since the information is "from the field", we call this set the ***bottom up*** set.
- Now suppose that we have an exceptions list of principal IDs. Since this list is axiomatic, we call it the ***top down*** set.

## Problem statement
Is there a satisfiable solution to the following problem: there exists a principal ID in the ***bottom up*** sets which isn't redundant in the  ***top down*** set

If the answer is "Yes", then this should raise an anomaly in our control framework, because we have found an unexpected user that doesn't belong to the exceptions list.

In the Python sample, users John and Jack belong to the exception list, but Julia doesn't. 

Users from ground truth are associated with the following booleans: bottomUp 1 for John, bottomUp 2 for JAck, bottomUp 3 for Julia.

Julia pops up from ground truth, but since she is not in the top down list, her ID is not redundant. It means that the boolean associated to her ID is satisfiable.

## The ripTide algorithm

I found this algorithm while reading Microsoft Research's paper on secGuru. Here is how they put it:

![Alt text](https://github.com/labyrinthinesecurity/automatedReasoning/blob/main/recipes/ripTide/ripTideAlgo.PNG)

