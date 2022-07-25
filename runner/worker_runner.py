import json
import re

from workers.worker_register import worker_register
from settings import logger


class WorkerRunner:

    def __call__(self, event, context):
        logger.info('Start worker runner')

        for record in event['Records']:
            logger.info('Getting worker_id')
            worker_id = self.get_worker_id_from_sqs_name(record)

            logger.info('worker_id: %d', worker_id)
            worker = worker_register.get_worker_by_id(worker_id)

            logger.info('Running worker')
            instance = worker()
            instance(event, context)

            logger.info('Finish worker')

        response = {
            "statusCode": 200,
            "body": json.dumps({'message': 'OK'})
        }
        return response

    def get_worker_id_from_sqs_name(self, record):
        sqs_name = record['eventSourceARN']
        worker_id = re.search(
            r'arn:aws:sqs:us-east-(1|2):(\d+):worker_(?P<worker_id>\d+)',
            sqs_name
        )
        if worker_id is None:
            raise Exception(f'worker_id not found in {sqs_name}')

        return int(worker_id.group('worker_id'))
