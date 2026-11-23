import boto3
import json

table = boto3.resource("dynamodb").Table("table1")

def lambda_handler(event, context):
    order_id = event["pathParameters"]["id"]

    response = table.get_item(
        Key={"partikey": order_id}
    )

    order = response.get("Item")

    return {
        "statusCode": 200 if order else 404,
        "body": json.dumps(
            order if order else {"error": "Order not found"}
        )
    }
