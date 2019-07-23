# CommandLogger

A custom readline compatible shell which logs timestamps and their output.

# Installation

```
python setup.py install
```

# Usage

In order to invoke the shell, the following command can be executed `cmd-logger` - this command can accept multiple command line options.

```
usage: cmd-logger [-h] [--command-log COMMAND_LOG] [--output-log]
                  [--output-log-dir OUTPUT_LOG_DIR] [--interval INTERVAL]
                  [--execute EXECUTE]

optional arguments:
  -h, --help            show this help message and exit
  --command-log COMMAND_LOG, -c COMMAND_LOG
                        Command log
  --output-log, -o      Enable output logging
  --output-log-dir OUTPUT_LOG_DIR, -d OUTPUT_LOG_DIR
                        Output log directory
  --interval INTERVAL, -i INTERVAL
                        Interval between command execution
  --execute EXECUTE, -e EXECUTE
                        List of commands to execute within intervals
```

The shell once invoked can accept a limited amount of interactive arguments, these can be found by typing `?` or `help`.

```
Welcome to the CommandLogger shell. Type help or ? to list commands.

2019-07-23 22:57:28> help

Documented commands (type help <topic>):
========================================
EOF  exit  help  interval  load  log  nolog  quit  show

2019-07-23 22:57:28>
```
