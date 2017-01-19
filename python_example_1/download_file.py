#!/usr/bin/python3
import boto3

s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)


# download a file
s3_client = boto3.client('s3')
s3_client.download_file('z0001-bucket', 't_0002.png', 't_0002.png')
