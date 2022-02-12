import json
import logging

import click

from robots.robot_register import robot_register


class RobotRunner:

    def __call__(self, event, context):
        try:
            robot_id = int(event['robot_id'])
        except KeyError:
            logging.error('Event has not robot_id')
            response = {
                'statusCode': 500,
                'body': json.dumps({
                    'message': 'Event has not robot_id',
                })
            }
            return response

        try:
            robot = robot_register.get_robot_by_id(robot_id)
        except Exception:
            logging.exception('An error happend when trying to get robot')
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
            logging.exception('An error happend during the robot execution')
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


def run_robot(event, context):
    runner = RobotRunner()
    return runner(event, context)


@click.group()
def cli():
    pass


@cli.command()
@click.option('--robot-id', required=True, type=int)
def run(robot_id):
    return run_robot({'robot_id': robot_id}, {})


if __name__ == '__main__':
    cli()
