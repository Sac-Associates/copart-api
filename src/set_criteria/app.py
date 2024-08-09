import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('UserCriteriaTable')

    body = json.loads(event['body'])
    user_id = event['requestContext']['authorizer']['claims']['sub']

    table.put_item(
        Item={
            'user_id': user_id,
            **body
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Criteria saved successfully!')
    }
