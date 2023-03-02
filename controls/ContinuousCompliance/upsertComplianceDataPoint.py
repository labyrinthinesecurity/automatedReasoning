from azure.data.tables import TableServiceClient,UpdateMode

connection_string = "***"

table_service = TableServiceClient.from_connection_string(conn_str=connection_string)
ledger = table_service.get_table_client(table_name="myComplianceActivityLogTable")


def upsert(entity1):
  global ledger
  insert_entity = ledger.upsert_entity(mode=UpdateMode.REPLACE, entity=entity1)
  print("Inserted entity: {}".format(insert_entity))

def createEntity(part,row,dayHour,startt,endt,md5sum,status,cached):
              entity = {
                "PartitionKey": part,
                "RowKey": row,
                "dayHour": dayHour,
                "startTime": startt,
                "finishTime": endt,
                "status": status
                }
              return entity
