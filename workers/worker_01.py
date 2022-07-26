import json

import boto3

from settings import logger
from workers.base_worker import BaseWorker
from workers.worker_register import worker_register


sqs_client = boto3.client('sqs')

@worker_register
class Worker01(BaseWorker):
    worker_id = 1

    def run(self, record):
        logger.info('Worker %s', self.worker_id)
        logger.info('Record: %s', record)

        msg = json.loads(record['body'])

        response = sqs_client.send_message(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/986806511625/worker_cron',
            MessageBody=json.dumps(msg),
        )

        logger.info('SQS Response: %s', response)
