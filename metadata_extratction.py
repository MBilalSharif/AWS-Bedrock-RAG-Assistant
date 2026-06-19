import json
import os
import boto3

s3 = boto3.client("s3")

# Map AWS services to categories
SERVICE_CATEGORY = {
    "ec2": "Compute",
    "lambda": "Compute",
    "ecs": "Compute",
    "eks": "Containers",

    "s3": "Storage",
    "efs": "Storage",
    "ebs": "Storage",
    "fsx": "Storage",

    "iam": "Security",
    "kms": "Security",
    "cognito": "Security",
    "secretsmanager": "Security",

    "vpc": "Networking",
    "route53": "Networking",
    "cloudfront": "Networking",

    "rds": "Database",
    "dynamodb": "Database",
    "redshift": "Database",

    "cloudwatch": "Monitoring",
    "cloudtrail": "Monitoring",

    "bedrock": "AI/ML",
    "sagemaker": "AI/ML",

    "leave": "HR"
}


def lambda_handler(event, context):

    # Get bucket and uploaded file
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    # Only process PDFs
    if not key.lower().endswith(".pdf"):
        return {
            "statusCode": 200,
            "message": "Not a PDF."
        }

    # Extract filename without extension
    filename = os.path.splitext(os.path.basename(key))[0].lower()

    # Guess service name from filename
    service = None

    for aws_service in SERVICE_CATEGORY.keys():
        if aws_service in filename:
            service = aws_service.upper()
            category = SERVICE_CATEGORY[aws_service]
            break

    # Default values if service isn't recognized
    if service is None:
        service = "Unknown"
        category = "General"

    metadata = {
        "metadataAttributes": {
            "service": service,
            "category": category,
            "documentType": "UserGuide",
            "provider": "AWS",
            "language": "English"
        }
    }

    metadata_key = key + ".metadata.json"

    s3.put_object(
        Bucket=bucket,
        Key=metadata_key,
        Body=json.dumps(metadata, indent=4),
        ContentType="application/json"
    )

    return {
        "statusCode": 200,
        "message": f"Metadata created: {metadata_key}"
    }