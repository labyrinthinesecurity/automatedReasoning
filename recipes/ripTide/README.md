![Alt text](https://github.com/labyrinthinesecurity/automatedReasoning/blob/main/recipes/ripTide/monsterRipTide.png)

**ripTide** is an automated reasoning pattern which checks whether a principal Id belongs to an exceptions list.

- Suppose that, from ground truth, we collect a list of principal IDs belonging to a first set. Since the information is "from the field", we call this set the ***bottom up*** set.
- Now suppose that we have an exceptions list of principal IDs. Since this list is axiomatic, we call it the ***top down*** set.

The question to answer by a formal proof is the following: is there an ID in the ***bottom up*** sets which doesn"t belong to the ***top down*** set?
If the answer is "Yes", then this should raise an anomaly in our control framework.

In the Python sample, users John and Jack belong to the exception list, but Julia doesn't. If Julia pops up from ground truth, this is an anomaly.

## The ripTide algorithm

I found this algorithm while reading Microsoft Research's paper on secGuru. Here is how they put it:

![Alt text](https://github.com/labyrinthinesecurity/automatedReasoning/blob/main/recipes/ripTide/ripTideAlgo.PNG)

