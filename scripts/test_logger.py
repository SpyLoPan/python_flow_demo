from etl.common.logger import get_logger

logger = get_logger("demo")

logger.info("This is an INFO message")
logger.warning("This is a WARNING message")
logger.error("This is an ERROR message")
