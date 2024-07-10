import json
import boto3
from botocore.exceptions import ClientError
from decimal import Decimal

# Helper function to convert DynamoDB Decimal types to standard Python types
def decimal_default(obj):
    if isinstance(obj, Decimal):
        return int(obj) if obj % 1 == 0 else float(obj)
    raise TypeError

def lambda_handler(event, context):
    # Initialize the DynamoDB client
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('cloud-resume-challenge')
    
    try:
        # Get the item with ID 'visitors'
        response = table.get_item(Key={'ID': 'visitors'})
        item = response.get('Item')

        if not item:
            raise Exception("The item with ID 'visitors' does not exist in the table.")

        visitor_count = item['visitors']
        
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET,PUT",
                "Access-Control-Allow-Headers": "Content-Type",
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "count": visitor_count
            }, default=decimal_default),
        }
    except ClientError as e:
        # Log the error and return an error response
        print(f"ClientError: {e.response['Error']['Message']}")
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET,PUT",
                "Access-Control-Allow-Headers": "Content-Type",
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "An error occurred while retrieving the visitor count.",
                "details": e.response['Error']['Message']
            }),
        }
    except Exception as e:
        # Log any other exceptions and return an error response
        print(f"Exception: {str(e)}")
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET,PUT",
                "Access-Control-Allow-Headers": "Content-Type",
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "An unexpected error occurred.",
                "details": str(e)
            }),
        }
