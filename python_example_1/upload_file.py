import boto3

s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# upload a new file
data = open(r'c:\work\test_images\test_images_small\t_0003.png', 'rb')
s3.Bucket('z0001-bucket').put_object(Key='t_0003.png', Body=data)

# download a file
