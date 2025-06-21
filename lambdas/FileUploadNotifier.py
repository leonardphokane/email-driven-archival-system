import json
import boto3
import os

ses = boto3.client('ses')
SENDER = os.environ.get("SENDER_EMAIL")  # e.g. leonardphokane1@gmail.com
RECIPIENT = os.environ.get("RECIPIENT_EMAIL")  # can be same as SENDER

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    # Extract bucket and file info
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        subject = f"New File Uploaded: {key}"
        body = f"A new file was uploaded to {bucket}:\n\n{key}\n\nTo archive this file, reply with:\nDelete {key}"

        response = ses.send_email(
            Source=SENDER,
            Destination={"ToAddresses": [RECIPIENT]},
            Message={
                "Subject": {"Data": subject},
                "Body": {"Text": {"Data": body}}
            }
        )
        print("Email sent:", response)

    return {"statusCode": 200, "body": "Notification sent"}
