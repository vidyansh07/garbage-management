import boto3
from django.conf import settings

def get_s3_client():
    return boto3.client('s3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME
    )

def upload_file_to_s3(file, filename):
    s3_client = get_s3_client()
    try:
        s3_client.upload_fileobj(file, settings.AWS_STORAGE_BUCKET_NAME, filename)
        return f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{filename}"
    except Exception as e:
        print(f"Error uploading file to S3: {str(e)}")
        return None