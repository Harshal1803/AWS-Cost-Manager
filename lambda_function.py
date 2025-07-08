import boto3
from datetime import datetime, timedelta
from twilio.rest import Client
import os

TWILIO_SID = os.environ['TWILIO_SID']
TWILIO_AUTH = os.environ['TWILIO_AUTH']
FROM_WA = os.environ['FROM_WA']
TO_WA = os.environ['TO_WA']


ce = boto3.client('ce')
ses = boto3.client('ses', region_name='eu-north-1')
twilio_client = Client(TWILIO_SID, TWILIO_AUTH)

def lambda_handler(event, context):
    today = datetime.utcnow().date()
    start = (today - timedelta(days=1)).strftime('%Y-%m-%d')
    end = today.strftime('%Y-%m-%d')

    response = ce.get_cost_and_usage(
        TimePeriod={'Start': start, 'End': end},
        Granularity='DAILY',
        Metrics=['UnblendedCost'],
        GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
    )

    message = f"AWS DAILY REPORT for {start}\n"
    for group in response['ResultsByTime'][0]['Groups']:
        service = group['Keys'][0]
        amount = float(group['Metrics']['UnblendedCost']['Amount'])
        if amount > 0:
            message += f"• {service}: ${amount:.2f}\n"

    twilio_client.messages.create(
        from_=FROM_WA,
        to=TO_WA,
        body=message
    )        

    return {"status": "Report sent successfully"}