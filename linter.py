#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Cory Locklear
# Copyright (c) 2017 Cory Locklear
#
# License: MIT

"""This module exports the Gosimple plugin class."""

from SublimeLinter.lint import Linter, util, highlight


class Gosimple(Linter):
    """Provides an interface to gosimple."""

    syntax = ('go', 'gosublime-go')
    cmd = 'gosimple'
    regex = r'^.+:(?P<line>\d+):(?P<col>\d+):\s+(?P<message>.+)'
    tempfile_suffix = 'gosimple'
    error_stream = util.STREAM_STDOUT
    default_type = highlight.WARNING
