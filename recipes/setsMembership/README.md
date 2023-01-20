![Alt text](https://github.com/labyrinthinesecurity/automatedReasoning/blob/main/recipes/setsMembership/monsterRipTide.png)

**ripTide** is an automated reasoning pattern to check if a set member belongs to another set, i.e. to check sets intersection and sets difference.

It solves a wide range of group membership problems.

- Suppose that, from ground truth, we collect a list of principal IDs belonging to a first set. Since the information is "from the field", we call this set the ***bottom up*** set.
- Now suppose that we have an exceptions list of principal IDs. Since this list is axiomatic, we call it the ***top down*** set.

## Problem statement
Is there a satisfiable solution to the following problem: there exists a principal ID in the ***bottom up*** sets which isn't redundant in the  ***top down*** set

If the answer is "Yes", then this should raise an anomaly in our control framework, because we have found an unexpected user that doesn't belong to the exceptions list.

## Python solution sample: how it works?

In the Python sample, users John and Jack belong to the exception list, but Julia doesn't: 

- Users from ground truth are associated with the following booleans: bottomUp 1 for John, bottomUp 2 for Jack, bottomUp 3 for Julia.

```
sol.add(ruleBottomUp1==Or(principalId==JOHN))
sol.add(ruleBottomUp2==Or(principalId==JACK))
sol.add(ruleBottomUp3==Or(principalId==JULIA))
```

- Users from the exception lists are associated with similar booleans: topDown 1 for Joh,n topDown 2 for Jack.

```
sol.add(ruleTopDown1==Or(principalId==JOHN))
sol.add(ruleTopDown2==Or(principalId==JACK))
```

The bitwise sets intersection logic is prepared as follows:

```
sol.add(P==Or(ruleTopDown1,ruleTopDown2,ruleBottomUp1,ruleBottomUp2,ruleBottomUp3))
sol.add(Q==Or(And(ruleTopDown1,bitTopDown1),And(ruleTopDown2,bitTopDown2),And(ruleBottomUp1,bitBottomUp1),And(ruleBottomUp2,bitBottomUp2),And(ruleBottomUp3,bitBottomUp3)))
sol.add(Q!=P)
```

To check whether Julia pops up from ground truth, we prepare this satisfiability statement:
```
sol.push()
sol.add(And(bitTopDown1,bitTopDown2,bitBottomUp1,bitBottomUp2,Not(bitBottomUp3)))
sol.check()
```

Since Julia is not in the top down list, this statement is satisfiable: her ID is not redundant. 


## The ripTide algorithm

I found this algorithm while reading Microsoft Research's paper on secGuru. Here is how they put it:

![Alt text](https://github.com/labyrinthinesecurity/automatedReasoning/blob/main/recipes/setsMembership/ripTideAlgo.PNG)

The original paper: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/secguru.pdf
