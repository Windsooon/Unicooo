#!/usr/bin/env python
# coding=utf-8
import sys
reload(sys)
sys.setdlopenflags("utf-8")

from handlers.index import InderHandler

url = [
    (r'/', IndexHandler),
]
