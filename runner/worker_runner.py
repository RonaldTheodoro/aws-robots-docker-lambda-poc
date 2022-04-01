import json

from workers.worker_register import worker_register
from settings import logger


class WorkerRunner:

    def __call__(self, event, context):
        try:
            worker_id = int(event['worker_id'])
        except KeyError:
            logger.error('Event has not worker_id')
            response = {
                'statusCode': 500,
                'body': json.dumps({
                    'message': 'Event has not worker_id',
                })
            }
            return response

        try:
            worker = worker_register.get_worker_by_id(worker_id)
        except Exception:
            logger.exception('An error happend when trying to get worker')
            response = {
                'statusCode': 500,
                'body': json.dumps({
                    'message': 'An error happend when trying to get worker',
                })
            }
            return response

        try:
            instance = worker()
            instance(event, context)
        except Exception:
            logger.exception('An error happend during the worker execution')
            response = {
                'statusCode': 500,
                'body': json.dumps({
                    'message': 'An error happend during the worker execution',
                })
            }
            return response

        response = {
            "statusCode": 200,
            "body": json.dumps({'message': 'OK'})
        }
        return response
