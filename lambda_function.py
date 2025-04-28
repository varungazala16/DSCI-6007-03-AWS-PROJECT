import json
import requests
import boto3
from datetime import datetime
# API Configuration
API_KEY = "JCG5X2C779JIPJS4"
STOCK_SYMBOL = "IBM"
API_URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK_SYMBOL}&interval=5min&apikey={API_KEY}&datatype=csv"
# AWS S3 Configuration
S3_BUCKET = "finalprojectstock"
s3_client = boto3.client("s3")
def lambda_handler(event, context):
    response = requests.get(API_URL)
    if response.status_code == 200:
        file_name = f"stocks/{STOCK_SYMBOL}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
# Upload CSV file to S3
        s3_client.put_object(
        Bucket=S3_BUCKET,
        Key=file_name,
        Body=response.content
    )
        return {
        "statusCode": 200,
        "body": f"Stock data for {STOCK_SYMBOL} stored in S3: {file_name}"
    }
    else:

        return {
            "statusCode": response.status_code,
            "body": "Failed to fetch stock data."
    }