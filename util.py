import os
import sys
import curses
import shlex
import six

import version

from functools import reduce

curses.setupterm()
e3_seq = curses.tigetstr('E3') or b''
clear_screen_seq = curses.tigetstr('clear') or b''

def clear_screen():
    os.write(sys.stdout.fileno(), e3_seq + clear_screen_seq)

def is_string(obj):
    if version.PY3:
        return isinstance(obj, str)
    else:
        return isinstance(obj, basestring)

def string_to_args(string):
    return shlex.split(string)

def is_mouse_event(key):
    return not isinstance(key, six.string_types)

def uuid_short(uuid):
    return uuid[0:8]

def task_id_or_uuid_short(task):
    return task['id'] or uuid_short(task['uuid'])
