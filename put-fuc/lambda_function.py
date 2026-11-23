import boto3
import json
from botocore.exceptions import ClientError

table = boto3.resource("dynamodb").Table("table1")

def lambda_handler(event, context):
    order_id = event["pathParameters"]["id"]
    data = json.loads(event["body"])

    try:
        response = table.update_item(
            Key={"partikey": order_id},
            UpdateExpression="SET #s = :s",
            ExpressionAttributeNames={"#s": "status"},
            ExpressionAttributeValues={":s": data["status"]},
            ConditionExpression="attribute_exists(partikey)",
            ReturnValues="ALL_NEW"
        )

        return {
            "statusCode": 200,
            "body": json.dumps(response["Attributes"])
        }

    except ClientError as error:
        if error.response["Error"]["Code"] == "ConditionalCheckFailedException":
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "Order not found"})
            }
        raise
