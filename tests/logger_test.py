from src import logger


logger = logger.Logger()

print("Test with source")
logger.info("info", source="TEST")
logger.debug("debug", source="TEST")
logger.warning("warning", source="TEST")
logger.error("error", source="TEST")
print("Test without source")
logger.info("info")
logger.debug("debug")
logger.warning("warning")
logger.error("error")

