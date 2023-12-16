import boto3
import csv

def lambda_handler(event, context):
    s3 = boto3.client('s3', endpoint_url='http://host.docker.internal:4566')
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        lines = response['Body'].read().decode('utf-8').splitlines()
        reader = csv.reader(lines)
        for row in reader:
            print(row)

# Test the function locally
if __name__ == '__main__':
    # Mock event
    test_event = {
        "Records": [
            {
                "s3": {
                    "bucket": {
                        "name": "test-data"
                    },
                    "object": {
                        "key": "test-file.csv"
                    }
                }
            }
        ]
    }

