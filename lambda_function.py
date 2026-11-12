import json
import os
import boto3

dynamodb = boto3.resource("dynamodb")

def lambda_handler(event, context):
    table_name = os.environ.get("TABLE_NAME", "SATC-Products")
    table = dynamodb.Table(table_name)

    response = table.scan()
    items = response.get("Items", [])

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(items, default=str)
    }
