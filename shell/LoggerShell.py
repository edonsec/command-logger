import cmd
import time
import subprocess
from shell import ExitShellException


class LoggerShell(cmd.Cmd):
    intro = "Welcome to the CommandLogger shell. " \
            "Type help or ? to list commands.\n"
    prompt = "> "

    def __init__(self, utility, logging, command_interval):
        cmd.Cmd.__init__(self)
        self.command_interval = command_interval
        self.utility = utility
        self.logging = logging

    def get_log_name(self):
        return "{}.log".format(int(time.time()))

    def output_formatted(self, cmdline, stdout, stderr):
        output = "Command: {}\n".format(cmdline)
        output += "Timestamp: {}\n".format(self.utility.clean_date_stamp())

        if self.logging.is_logging():
            output += "Logname: {}\n".format(self.get_log_name())

        if stdout:
            output += "=== OUTPUT ===\n"
            output +=  stdout

        if stderr:
            output += "=== ERROR ===\n"
            output += stderr

        return output

    def default(self, line):
        command_ts = "{} {}".format(self.utility.clean_date_stamp(), line)

        print command_ts
        self.logging.write_command_log(command_ts + "\n")

        shell_exec = subprocess.Popen(line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout,stderr = shell_exec.communicate()

        output = self.output_formatted(line, stdout, stderr)

        print output

        self.logging.write_log(self.get_log_name(), output)

    def do_show(self, args):
        with open(self.logging.get_command_log(), "r") as f:
            print f.read()

    def help_show(self):
        print "Display command log without logging entry"

    def do_load(self, args):
        with open(args, "r") as f:
            for line in f:
                self.onecmd(line)
                time.sleep(int(self.command_interval))

    def help_load(self):
        print "load <filename> - Load a list of commands to execute and log timestamps"

    def do_nolog(self, args):
        print "Logging disabled"
        self.logging.disable_logging()

    def help_nolog(self):
        print "Disable logging to file"

    def do_interval(self, args):
        self.command_interval = args

    def help_interval(self):
        print "interval <second> - Amount of seconds to wait between each request"

    def do_log(self, args):
        print "Logging enabled"
        self.logging.enable_logging()

    def help_log(self):
        print "Enable logging to file"

    def do_exit(self, args):
        raise ExitShellException

    def help_exit(self):
        print("Quit from shell")

    def set_prompt_name(self, name):
        self.prompt = "{}> ".format(name)

    do_quit = do_exit
    help_quit = help_exit
    do_EOF = do_exit
    help_EOF = help_exit
