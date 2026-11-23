import boto3
import json
import uuid

table = boto3.resource("dynamodb").Table("table1")

def lambda_handler(event, context):
    data = json.loads(event["body"])

    order = {
        "partikey": str(uuid.uuid4()),
        "product": data["product"],
        "status": "new"
    }

    table.put_item(Item=order)

    return {
        "statusCode": 201,
        "body": json.dumps(order)
    }
