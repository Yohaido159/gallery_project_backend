import boto3
from gal_pro.secret import *


def send_sms():
    print("start")
    sns = boto3.client('sns',
                       aws_access_key_id=AWS_ACCESS_KEY_ID,
                       aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                       region_name="us-east-1"
                       )
    Number = '+972504035559'
    Message = 'Simple text message'
    sns.publish(
        PhoneNumber=Number, Message=Message
    )
