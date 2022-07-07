import logging


logging.basicConfig(
    format='%(asctime)s [%(process)d] %(levelname)s %(name)s: %(message)s',
    level=logging.DEBUG,
    force=True
)
logger = logging.getLogger('workers poc')
