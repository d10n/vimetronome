#!/usr/bin/env python
# cli.py
# -*- coding: utf8 -*-

"""vimetronome, a CLI visual metronome

Usage:
  vimetronome <bpm>
  vimetronome (--help | --version)
"""

import sys
import time
from schema import Schema, SchemaError, Use
from docopt import docopt

from vimetronome.metronome import Metronome


def main():
    args = parse_args()
    seconds = 60. / args['<bpm>']
    m = Metronome()
    while True:
        m.tick()
        time.sleep(seconds)
    pass


def parse_args() -> dict:
    args = docopt(sys.modules[__name__].__doc__, version='0.1.0')
    schema = Schema({'<bpm>': Use(int)}, ignore_extra_keys=True)
    try:
        args = schema.validate(args)
    except SchemaError as e:
        exit(e)
    return args


if __name__ == '__main__':
    main()
