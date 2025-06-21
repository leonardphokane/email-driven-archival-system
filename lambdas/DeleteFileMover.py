import json
import boto3
import email
import os

s3 = boto3.client('s3')

UPLOAD_BUCKET = os.environ.get('UPLOAD_BUCKET')        # e.g. leonard-upload-bucket-2025
ARCHIVE_BUCKET = os.environ.get('ARCHIVE_BUCKET')      # e.g. leonard-archive-bucket-2025

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))

    # Extract email from S3
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']

        response = s3.get_object(Bucket=bucket, Key=object_key)
        raw_email = response['Body'].read().decode('utf-8')

        # Parse subject or body
        msg = email.message_from_string(raw_email)
        subject = msg.get('Subject', '')
        body = ""

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    body += part.get_payload(decode=True).decode('utf-8', errors='ignore')
        else:
            body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')

        print("Parsed subject:", subject)
        print("Parsed body:", body)

        # Check for "Delete filename"
        command_text = subject + "\n" + body
        lines = command_text.splitlines()

        for line in lines:
            if line.strip().lower().startswith("delete "):
                target_file = line.strip()[7:].strip()
                source_key = f"uploads/{target_file}"
                dest_key = f"archive/{target_file}"

                try:
                    # Copy to archive bucket
                    s3.copy_object(
                        Bucket=ARCHIVE_BUCKET,
                        CopySource={'Bucket': UPLOAD_BUCKET, 'Key': source_key},
                        Key=dest_key
                    )
                    # Delete original
                    s3.delete_object(Bucket=UPLOAD_BUCKET, Key=source_key)
                    print(f"Moved {source_key} to archive as {dest_key}")
                except Exception as e:
                    print(f"Error archiving file: {e}")
