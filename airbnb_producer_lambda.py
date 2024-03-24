import boto3
import random
from datetime import datetime, timedelta
import json

sqs_client = boto3.client('sqs', region_name = 'us-east-1')
SQL_QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/717085097847/sqs-airbnb-topic"

def random_data_generator():
    start_date = (datetime(2023,1,1)+timedelta(days=random.randint(0,300)))
    end_date = start_date+timedelta(days=random.randint(0,10))
    return {
        "bookingId":random.randint(1,100000),
        "userId": "U"+str(random.randint(1,10000)),
        "propertyId":"P"+str((random.randint(1,1000))),
        "location":random.choice(['Panaji,India','Gandhinagar,India','Chandigarh,India','Ranchi,India','Bangalore,India']),
        "startDate": start_date.strftime("%Y-%m-%d"),
        "endDate": end_date.strftime("%Y-%m-%d"),
        "price": random.randint(10,2000)
    }

def lambda_handler(event, context):

    i=0
    while i<30:
        data = json.dumps(random_data_generator())
        res = sqs_client.send_message(QueueUrl = SQL_QUEUE_URL, MessageBody = data )
        print(data)
        i= i+1






