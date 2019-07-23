import argparse

from logging import Logging
from shell import ExitShellException
from shell.LoggerShell import LoggerShell
from utility import Utility
import time


def main():
    parser = argparse.ArgumentParser()

    try:
        parser.add_argument("--command-log", "-c", help="Command log", default="commands.txt")
        parser.add_argument("--output-log", "-o", help="Enable output logging", action="store_true")
        parser.add_argument("--output-log-dir", "-d", help="Output log directory")
        parser.add_argument("--interval", "-i", help="Interval between command execution")
        parser.add_argument("--execute", "-e", help="List of commands to execute within intervals")

        parser.set_defaults(output_log=False, interval=0)

        args = parser.parse_args()
        utility = Utility()
        logging = Logging(args.command_log, args.output_log)

        logger_shell = LoggerShell(utility, logging, args.interval)

        if args.execute:
            print logger_shell.onecmd('load' + args.execute)

        logger_shell.set_prompt_name(utility.clean_date_stamp())

        logger_shell.cmdloop()
    except ExitShellException:
        pass
