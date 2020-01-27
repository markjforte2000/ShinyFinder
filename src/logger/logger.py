from datetime import datetime


class Logger(object):

    def __init__(self):
        # default format
        # "[TIME] [TYPE] [SOURCE]: MESSAGE"
        self.default_format_source = "[{0}] [{1}] [{2}]: {3}"
        self.default_format_no_source = "[{0}] [{1}]: {2}"
        self.info_flag = "INFO"
        self.debug_flag = "DEBUG"
        self.warning_flag = "WARNING"
        self.error_flag = "ERROR"
        return

    def _log(self, log_type, data, source=None):
        now = datetime.now()
        now = now.strftime("%m-%d-%Y %H:%M:%S")
        if source is None:
            message = self.default_format_no_source.format(now, log_type, data)
        else:
            message = self.default_format_source.format(now, log_type, source, data)
        print(message)
        return

    def info(self, data, source=None):
        self._log(self.info_flag, data, source)
        return

    def debug(self, data, source=None):
        self._log(self.debug_flag, data, source)
        return

    def warning(self, data, source=None):
        self._log(self.warning_flag, data, source)
        return

    def error(self, data, source=None):
        self._log(self.error_flag, data, source)
        return

