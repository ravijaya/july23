"""log parser aka unix grep command"""
import re
from fileinput import input as stream_reader, filelineno, filename  # unix command
# the above input called as stream reader


def grep_me(pattern, fname):
    """
    to implement unix like grep
    :param pattern: regular expression
    :param fname: file_name
    :return: None
    """
    for line in stream_reader(fname):
        if re.search(pattern, line, re.I):
            print('{}:{}:{}'.format(filename(), filelineno(), line), end='')



