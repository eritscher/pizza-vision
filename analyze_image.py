import boto3
from os import getenv


def analyze_image(image):
    ACCESS_KEY = getenv('AWS_ACCESS_KEY')
    SECRET = getenv('AWS_SECRET_ACCESS_KEY')
    client = boto3.client('rekognition', aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET)
    response = client.detect_labels(Image={'Bytes': image.read()})

    return response['Labels']


if __name__ == "__main__":
    print('Do not run analyze_image directly, use it as part of the API.')
