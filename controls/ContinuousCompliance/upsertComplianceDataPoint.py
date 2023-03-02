from azure.data.tables import TableServiceClient,UpdateMode
import datetime, time

connection_string = "***"

table_service = TableServiceClient.from_connection_string(conn_str=connection_string)
ledger = table_service.get_table_client(table_name="myComplianceActivityLogTable")


def upsert(entity1):
  global ledger
  insert_entity = ledger.upsert_entity(mode=UpdateMode.REPLACE, entity=entity1)
  print("Inserted entity: {}".format(insert_entity))

def createEntity(part,row,dayHour,startt,endt,md5sum,status):
              entity = {
                "PartitionKey": part,
                "RowKey": row,
                "dayHour": dayHour,
                "startTime": startt,
                "finishTime": endt,
                "status": status
                }
              return entity

    

status='OK'
currentMonth = datetime.datetime.now().month
currentYear = datetime.datetime.now().year
currentHour = datetime.datetime.now().hour
partition=str(currentYear)+"-"+str(currentMonth)
start=int(math.floor(time.time()))
finish=int(math.floor(time.time()))
auid="abcd"

ce=createEntity(partition,auid,currentHour,str(start),str(finish),status)
print(ce)
upsert(ce)
