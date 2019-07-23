class Logging(object):
    def __init__(self, do_command_log, do_log):
        self.do_command_log = do_command_log
        self.do_log = do_log

    def write_command_log(self, command, mode="a+"):
        if self.do_command_log and self.do_command_log != "":
            self._write_to_file(self.do_command_log, command, mode)

    def write_log(self, filename, output, mode="a+"):
        if self.do_log:
            self._write_to_file(filename, output, mode)

    def _write_to_file(self, filename, contents, mode="a+"):
        with open(filename, mode) as f:
            f.write(contents)

    def get_command_log(self):
        return self.do_command_log

    def is_logging(self):
        return self.do_log

    def disable_logging(self):
        self.do_log = False

    def enable_logging(self):
        self.do_log = True

