import json

import boto3

from settings import logger
from workers.base_worker import BaseWorker
from workers.worker_register import worker_register


sqs_client = boto3.client('sqs')

@worker_register
class Worker01(BaseWorker):
    worker_id = 1

    def run(self, event, context):
        logger.info('Worker 01')
        logger.info('Event: %s', event)

        msg = json.loads(event['body'])

        response = sqs_client.send_message(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/986806511625/worker_cron',
            MessageBody=json.dumps(msg),
        )

        logger.info('SQS Response: %s', response)
