import logging


logging.basicConfig(
    format='%(asctime)s [%(process)d] %(levelname)s %(name)s: %(message)s',
    level=logging.DEBUG
)
logger = logging.getLogger('workers poc')
