import boto3

from django.conf import settings
from django.core.mail import send_mail

from celery import shared_task


@shared_task
def task_send_mail_utils_password(password, email):

    print("Sending Email")
    send_mail(
        'Utils Password',
        f'the password of utils is {password}.',
        'yohaido159@gmail.com',
        [f'{email}'],
    )


@shared_task
def task_send_sms_utils_password(password, phone):

    print("Sending Sms")
    if phone[0:4] == "+972":
        phone = phone
    else:
        phone = phone[1:]
        phone = f"+972{phone}"

    client = boto3.client('sns',
                          aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                          region_name=settings.REGION_NAME
                          )
    client.publish(Message=f"the password of utils is {password}", PhoneNumber=phone)
