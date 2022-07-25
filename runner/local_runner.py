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
            sqs_event = {
                'Records': [
                    {
                        'body': json.dumps(event['body']),
                        'eventSourceARN': event['sqs_queue'],
                    }
                ]
            }
            yield sqs_event
