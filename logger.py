import logging


logging.basicConfig(
    format='%(asctime)s [%(process)d] %(levelname)s %(name)s: %(message)s',
    level=logging.DEBUG,
    force=True
)
logger = logging.getLogger('workers poc')


loggers_name = [
    'boto3',
    'botocore',
    'botocore.hooks',
    'botocore.utils',
    'botocore.credentials',
    'botocore.loaders',
    'botocore.endpoint',
    'botocore.client',
    'nose',
    'urllib3.connectionpool',
]

for logger_name in loggers_name:
    logging.getLogger(logger_name).setLevel(logging.INFO)

