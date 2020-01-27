from src import logger

from os import remove


# default config test
print("-- DEFAULT OUTPUTS TEST --")
lgr = logger.Logger()

print("Test with source")
lgr.info("info", source="TEST")
lgr.debug("debug", source="TEST")
lgr.warning("warning", source="TEST")
lgr.error("error", source="TEST")
print("Test without source")
lgr.info("info")
lgr.debug("debug")
lgr.warning("warning")
lgr.error("error")

# output with file
log_file = open("log_test_file.txt", "w")
lgr2 = logger.Logger(log_file=log_file)

print("-- MULTIPLE OUTPUTS TEST --")

lgr2.info("info", source="TEST2")
lgr2.debug("debug", source="TEST2")
lgr2.warning("warning", source="TEST2")
lgr2.error("error", source="TEST2")

log_file.close()

print("Check log_test_file.txt")
print("Then press enter")
input()
remove("log_test_file.txt")

