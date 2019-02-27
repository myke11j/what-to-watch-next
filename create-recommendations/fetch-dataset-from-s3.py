import boto3
import os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BUCKET_NAME = os.environ.get("BUCKET_NAME")
KEY_NAME = os.environ.get("KEY_NAME")

def download_dir(client, resource, local='./tmp/', bucket='', key=''):
    my_bucket = resource.Bucket(bucket)
    for s3_object in my_bucket.objects.all():
        if(s3_object.key != key):
            path, filename = os.path.split(s3_object.key)
            client.download_file(bucket, s3_object.key, local + filename)

def downlodDataset(bucketName, keyName):
    client = boto3.client('s3')
    resource = boto3.resource('s3')
    download_dir(client, resource, './tmp/', bucketName, keyName)

if __name__ == '__main__':
    downlodDataset(BUCKET_NAME, KEY_NAME)