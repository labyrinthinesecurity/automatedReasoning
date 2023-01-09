import hashlib
from uuid import *

def addPrincipal(principalId):
  aVal=abs(hash(principalId))
  globals()[principalId]=None
  principalIdInt=Const(principalId,IntSort())
  return aVal

sol=Solver()
GREEN_JOHN=addPrincipal('f895073d-5b67-4809-bea4-df1d5bc1d12e')
GREEN_JACK=addPrincipal('90aa079a-12df-472a-a11c-4a548cb04fea')
BLUE_JULIA=addPrincipal('6c48bb71-a99e-4466-a998-92b51ecd6859')

principalId=Const('principalId',IntSort())
ruleTopDown1,ruleTopDown2,ruleBottomUp1,ruleBottomUp2,ruleBottomUp3=Consts('ruleTopDown1 ruleTopDown2 ruleBottomUp1 ruleBottomUp2 ruleBottomUp3',BoolSort())
bitTopDown1,bitTopDown2=Consts('bitTopDown1 bitTopDown2',BoolSort())
bitBottomUp1,bitBottomUp2,bitBottomUp3=Consts('bitBottomUp1 bitBottomUp2 bitBottomUp3',BoolSort())
P,Q=Consts('P Q',BoolSort())

sol.add(ruleTopDown1==Or(principalId==GREEN_JOHN))
sol.add(ruleTopDown2==Or(principalId==GREEN_JACK))
sol.add(ruleBottomUp1==Or(principalId==GREEN_JOHN))
sol.add(ruleBottomUp2==Or(principalId==GREEN_JACK))
sol.add(ruleBottomUp3==Or(principalId==BLUE_JULIA))

sol.add(P==Or(ruleTopDown1,ruleTopDown2,ruleBottomUp1,ruleBottomUp2,ruleBottomUp3))
sol.add(Q==Or(And(ruleTopDown1,bitTopDown1),And(ruleTopDown2,bitTopDown2),And(ruleBottomUp1,bitBottomUp1),And(ruleBottomUp2,bitBottomUp2),And(ruleBottomUp3,bitBottomUp3)))

sol.add(Q!=P)

sol.push()
sol.add(And(bitTopDown1,bitTopDown2,bitBottomUp1,bitBottomUp2,Not(bitBottomUp3)))
if sol.check()==sat:
  print('SAT BottomUp 3 is NOT redundant')
else:
  print('UNSAT BottomUp 3 is redundant')
sol.pop()

sol.push()
sol.add(And(bitTopDown1,bitTopDown2,bitBottomUp1,Not(bitBottomUp2),bitBottomUp3))
if sol.check()==sat:
  print('SAT BottomUp 2',sol)
else:
  print('UNSAT BottomUp 2 is redundant')
sol.pop()

sol.push()
sol.add(And(bitTopDown1,bitTopDown2,Not(bitBottomUp1),bitBottomUp2,bitBottomUp3))
if sol.check()==sat:
  print('SAT BottomUp 1',sol)
else:
  print('UNSAT BottomUp 1 is redundant')
sol.pop()
