import json

def lambda_handler(event, context):
    return {
        'statusCode': '200',
        'body': """{"hello":"world"}""",
        'headers': {
            'Content-Type': 'application/json',
        },
    }