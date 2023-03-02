#!/usr/bin/python3 -u
from z3 import *
import random,math,sys,json,math
import hashlib
from uuid import *
import subprocess
from azure.data.tables import TableServiceClient,UpdateMode
import datetime,time

connection_string = "DefaultEndpointsProtocol=https;AccountName=***"

table_service = TableServiceClient.from_connection_string(conn_str=connection_string)
ledger = table_service.get_table_client(table_name="myComplianceActivityLogsTable")

sol=Solver()
t=BitVec('t',32)
phi=None
GRACE=600

now=int(math.floor(time.time()))

currentMonth = datetime.datetime.now().month
currentYear = datetime.datetime.now().year
currentDay = datetime.datetime.now().day
currentHour = datetime.datetime.now().hour
minPeriodTime=datetime.datetime(currentYear,currentMonth,1,0,0)
minPeriodTimeStamp=int(time.mktime(minPeriodTime.timetuple()))
nextPeriodMonth=currentMonth+1
nextPeriodYear=currentYear
if nextPeriodMonth>12:
  nextPeriodMonth=1
  nextPeriodYear=nextPeriodYear+1
maxPeriodTime=datetime.datetime(nextPeriodYear,nextPeriodMonth,1,0,0)
maxPeriodTimeStamp=min(now,int(time.mktime(maxPeriodTime.timetuple())))-GRACE
if maxPeriodTimeStamp<minPeriodTimeStamp:
  maxPEriodTimeStamp=minPeriodTimeStamp
partition=str(currentYear)+"-"+str(currentMonth)
dayHour=str(currentDay)+"-"+str(currentHour)
minute=str(datetime.datetime.now().minute)

tstamp=partition+':'+dayHour+':'+minute

def minBVSAT(phi,Sk):
  global t
  aL0=Sk[0]
#  print("aL0",aL0)
  B1=And(Not(phi),ULT(t,aL0))
  sol2=Solver()
  sol2.add(B1)
  while sol2.check()==sat:
    mdl=sol2.model()
    aL=mdl.evaluate(t).as_long()
    B1=And(B1,ULT(aL,t))
    sol2.add(B1)
  Sk[0]=aL+1
  return Sk

def maxBVSAT(phi,Sk):
  global t
  aL0=Sk[1]
  B2=And(Not(phi),UGT(t,aL0))
  sol2=Solver()
  sol2.add(B2)
  while sol2.check()==sat:
    mdl=sol2.model()
    aL=mdl.evaluate(t).as_long()
    B2=And(B2,UGT(aL,t))
    sol2.add(B2)
  Sk[1]=aL-1
  return Sk

def ALLBVSAT():
  global t
  global phi
  global sol
  B=phi
  k=-1
  S=[]
  sol.add(B)
  sol.check()
  while sol.check()==sat:
    k=k+1
    print('New interval',k)
    mdl=sol.model()
    aT=mdl.evaluate(t).as_long()
    I=[aT,aT]
    S.append(I)
    print("  assignment:",aT,end=' ')
    S[k]=maxBVSAT(phi,S[k])
    S[k]=minBVSAT(phi,S[k])
    print(S[k]," delta:",S[k][1]-S[k][0])
    S[k].append(S[k][1]-S[k][0])
    B=And(B,Or(UGT(t,S[k][1]),ULT(t,S[k][0])))
    sol.add(B)
  for aS in S:
    aS[0]=aS[0]*grain
    aS[1]=aS[1]*grain
  S.sort(key=lambda a: a[2], reverse=True)  # sort by third element in the tuple, i.e. highest delta
  return S

def loadCertificationPeriod(part,beginPeriod,endPeriod,grain):
  global ledger
  global sol
  global t
  phi=True
  cert=[]
  if part is None:
    lfilter = "PartitionKey le '\uffff'"
  else:
    lfilter = "PartitionKey eq \'"+part+"\'"
  entities = ledger.query_entities(lfilter)
  for entity in entities:
    aE={}
    for key in entity.keys():
      val=entity[key]
      if key=='startTime':
        val=int(math.floor(float(entity[key])/grain))
        aE['start']=val
      if key=='finishTime':
        val=int(math.ceil(float(entity[key])/grain))
        aE['finish']=val
    if (aE['start'] is not None) and (aE['finish'] is not None):
      cert.append(aE)
      phi=And(phi,Or(ULT(t,aE['start']),UGT(t,aE['finish'])))
  phi=And(UGE(t,beginPeriod),ULT(t,endPeriod),phi)
  return cert,phi

print("now:",dayHour+':'+minute,str(now))
print("partition:",partition)
print("ranging from",minPeriodTime,minPeriodTimeStamp,"to",maxPeriodTime,maxPeriodTimeStamp)

grain=1 # seconds
cert,phi=loadCertificationPeriod(partition,minPeriodTimeStamp,maxPeriodTimeStamp,grain)

minTime=now+9999999999999999999
maxTime=0
nbPoints=0
for aPoint in cert:
  if aPoint['start']<minTime:
    minTime=aPoint['start']
  if aPoint['finish']>maxTime:
    maxTime=aPoint['finish']
  nbPoints=nbPoints+1

print("points in period:",nbPoints)
if nbPoints==0:
      sys.exit()
deltaTime=maxTime-minTime
print("min/max times",str(grain*minTime),str(grain*maxTime),str(grain*deltaTime/(3600*24))+' days')

sol.add(phi)
print(ALLBVSAT())

endTime=int(math.floor(time.time()))
duration=endTime-now
print("SMT eval duration:",duration)
