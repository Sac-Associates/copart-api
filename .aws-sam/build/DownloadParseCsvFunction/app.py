import json
import boto3
import requests

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    url = "https://www.copart.com/downloadSalesData/"
    response = requests.get(url)

    if response.status_code == 200:
        s3.put_object(Bucket="copart-csv-storage", Key="latest_copart_data.csv", Body=response.content)
        return {
            'statusCode': 200,
            'body': json.dumps('CSV downloaded and uploaded to S3!')
        }
    else:
        return {
            'statusCode': response.status_code,
            'body': json.dumps('Failed to download CSV file.')
        }
