import logging

import watchtower

from settings.settings import settings


logging.basicConfig(
    format='%(asctime)s [%(process)d] %(levelname)s %(name)s: %(message)s',
    level=logging.DEBUG
)
logger = logging.getLogger('robots poc')

if settings.is_aws:
    logger.addHandler(watchtower.CloudWatchLogHandler())
