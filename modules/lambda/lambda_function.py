import boto3
import urllib.parse

s3 = boto3.client("s3")


def lambda_handler(event, context):

    print("S3 event received")

    for record in event["Records"]:

        bucket_name = record["s3"]["bucket"]["name"]
        object_key = urllib.parse.unquote_plus(
            record["s3"]["object"]["key"]
        )

        print(f"Bucket: {bucket_name}")
        print(f"Object: {object_key}")

        response = s3.get_object(
            Bucket=bucket_name,
            Key=object_key
        )

        content = response["Body"].read().decode("utf-8")

        print("Original content:")
        print(content)

        transformed_content = content.lower()

        print("Transformed content:")
        print(transformed_content)

        output_key = object_key.replace(
            "input/",
            "output/",
            1
        )

        s3.put_object(
            Bucket=bucket_name,
            Key=output_key,
            Body=transformed_content.encode("utf-8"),
            ContentType="text/plain"
        )

        print(f"Created: {output_key}")

    return {
        "statusCode": 200,
        "body": "File processed successfully"
    }
