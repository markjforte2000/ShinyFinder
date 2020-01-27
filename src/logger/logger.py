from datetime import datetime


class Logger(object):

    __info_flag = "INFO"
    __debug_flag = "DEBUG"
    __warning_flag = "WARNING"
    __error_flag = "ERROR"

    def __init__(self, log_file=None, automatic_file_writes=True):
        # default format
        # "[TIME] [TYPE] [SOURCE]: MESSAGE"
        # "[TIME] [TYPE]: MESSAGE"
        self.__default_format_source = "[{0}] [{1}] [{2}]: {3}"
        self.__default_format_no_source = "[{0}] [{1}]: {2}"
        # setup stream saving
        self.__sorted_stream = {
            self.__info_flag: [],
            self.__debug_flag: [],
            self.__warning_flag: [],
            self.__error_flag: []
        }
        self.__stream = []
        # log file
        self.__log_file = log_file
        self.__automatic_file_writes = automatic_file_writes
        return

    def __log(self, log_type, data, source=None):
        now = datetime.now()
        now = now.strftime("%m-%d-%Y %H:%M:%S")
        if source is None:
            message = self.__default_format_no_source.format(now, log_type, data)
        else:
            message = self.__default_format_source.format(now, log_type, source, data)

        self.__sorted_stream[log_type].append(message)
        self.__stream.append(message)
        print(message)
        if self.__log_file is not None and self.__automatic_file_writes:
            message = message + "\n"
            self.__log_file.write(message)
        return

    def write_to_file(self):
        if self.__log_file is not None:
            for message in self.__stream:
                self.__log_file.write(message)

    def info(self, data, source=None):
        self.__log(self.__info_flag, data, source)
        return

    def get_info(self):
        return self.__sorted_stream[self.__info_flag]

    def debug(self, data, source=None):
        self.__log(self.__debug_flag, data, source)
        return

    def get_debug(self):
        return self.__sorted_stream[self.__debug_flag]

    def warning(self, data, source=None):
        self.__log(self.__warning_flag, data, source)
        return

    def get_warning(self):
        return self.__sorted_stream[self.__warning_flag]

    def error(self, data, source=None):
        self.__log(self.__error_flag, data, source)
        return

    def get_error(self):
        return self.__sorted_stream[self.__error_flag]

    def get_stream(self):
        return self.__stream
