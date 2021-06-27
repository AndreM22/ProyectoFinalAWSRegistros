
import json
import boto3
import os

accounts_table = os.environ['ACCOUNTS-TABLE']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(accounts_table)


def putAccount(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    account_id = path.split("/")[-1] # ["account", "id"]
    
    body = json.loads(event["body"])
    print(body)
    print(account_id)
    item = {
        'pk': account_id,
        'name': body["name"],
        'money_amount': body["money_amount"],
        'business_info': body["business_info"],
        'monthly_salary': body["monthly_salary"]
    }
    print(json.dumps(item))
    table.put_item(
       Item=item
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }