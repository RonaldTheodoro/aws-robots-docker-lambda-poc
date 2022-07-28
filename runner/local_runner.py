import json

from runner import WorkerRunner
from settings import settings


class LocalRunner:

    def __init__(self):
        self.runner = WorkerRunner()

    def __call__(self, worker_id):
        payload_file_path = self.get_payload_file_path(worker_id)
        payload = self.get_payload_from_file_path(payload_file_path)
        for event in self.convert_payload_to_sqs_format(payload):
            self.runner(event, {})

    def get_payload_file_path(self, worker_id):
        payload_file_path = settings.payloads / f'{worker_id}.json'
        if not payload_file_path.exists():
            raise Exception(f'payload {worker_id}.json do not exists')
        return payload_file_path

    def get_payload_from_file_path(self, payload_file_path):
        with payload_file_path.open(mode='r') as fp:
            return json.load(fp)

    def convert_payload_to_sqs_format(self, payload):
        for event in payload:
            yield self.create_sqs_event(event)

    def create_sqs_event(self, event):
        sqs_event = {
            'Records': [
                {
                    'messageId': 'messageId',
                    'receiptHandle': 'receiptHandle',
                    'body': json.dumps(event['body']),
                    'messageAttributes': {},
                    'md5OfBody': '51a18d1e6f9dc116504f4d7125e867fb',
                    'eventSource': 'aws:sqs',
                    'eventSourceARN': event['sqs_queue'],
                    'awsRegion': 'us-east-1'
                }
            ]
        }
        return sqs_event
