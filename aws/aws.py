import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
    # Upload a new file
# data = open('swagger.json', 'rb')
# s3.Bucket('newdsource').put_object(Key='swagger.json', Body=data)

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)



