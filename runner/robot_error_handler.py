import json
import re

import boto3

from settings import settings


class RobotErrorHandler:

    def __init__(self) -> None:
        self.sqs_error_handler = SQSErrorHandler()

    def __call__(self, worker, record):
        try:
            instance = worker()
            instance(record)
        except Exception:
            self.sqs_error_handler.change_message_visibility(record)


class SQSErrorHandler:

    def __init__(self):
        self.sqs_client = boto3.client('sqs')

    def change_message_visibility(self, record):
        if settings.is_local:
            return

        self.sqs_client.change_message_visibility(
            QueueUrl=self.sqs_url(record),
            ReceiptHandle=record['receiptHandle'],
            VisibilityTimeout=300
        )

        self.sqs_client.send_message(
            MessageBody=record['body'],
            QueueUrl=self.sqs_url(record),
            DelaySeconds=30
        )

    def sqs_url(self, record):
        sqs_name = record['eventSourceARN']
        worker_id = re.search(
            r'^arn:aws:sqs:us-east-(1|2):(\d+):worker_(?P<worker_id>.*?)$',
            sqs_name
        )
        if worker_id is None:
            raise Exception(f'worker_id not found in {sqs_name}')

        worker_id = worker_id.group('worker_id')

        url_base = f'https://sqs.{settings.REGION}.amazonaws.com'
        return f'{url_base}/{settings.ACCOUNT_ID}/worker_{worker_id}'
