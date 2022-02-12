import json

from workers.worker_register import worker_register
from settings import logger


class WorkerRunner:

    def __call__(self, event, context):
        try:
            robot_id = int(event['robot_id'])
        except KeyError:
            logger.error('Event has not robot_id')
            response = {
                'statusCode': 500,
                'body': json.dumps({
                    'message': 'Event has not robot_id',
                })
            }
            return response

        try:
            robot = worker_register.get_robot_by_id(robot_id)
        except Exception:
            logger.exception('An error happend when trying to get robot')
            response = {
                'statusCode': 500,
                'body': json.dumps({
                    'message': 'An error happend when trying to get robot',
                })
            }
            return response

        try:
            instance = robot()
            instance(event, context)
        except Exception:
            logger.exception('An error happend during the robot execution')
            response = {
                'statusCode': 500,
                'body': json.dumps({
                    'message': 'An error happend during the robot execution',
                })
            }
            return response

        response = {
            "statusCode": 200,
            "body": json.dumps({'message': 'OK'})
        }
        return response
