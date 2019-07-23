from setuptools import setup

setup(
    name='CommandLogger',
    version='0.1',
    url='',
    license='',
    author='Ed Cradock',
    author_email='',
    description='A custom shell which logs date stamps for each command executed.',
    entry_points={
        "console_scripts": [
            "cmd-logger=cmd_logger:main"
        ]
    }
)
