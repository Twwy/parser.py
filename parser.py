#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Twwy
# Description: parse the argv in python
#
# python test.py xxx -a 1 --b 2 2 4 -t 
#
# data: {"default":["xxx"], "-a":["1"], "--b":["2","2","4"], "-t":[]}
#
#
# usage
#
# import parser
# parser.load()
# a = parser.read("-a")       # 1
# b = parser.read("--b")       # 2
# b1 = parser.readList("--b")  # ["2","2","4"]
# c = parser.read()          # xxx
# d = parser.read("--b","-a")   # 2
# e = parser.read("-e")       # None
# t = parser.read("-t")       # ""

import sys

data = {"default": []}

def load():
    if len(sys.argv[1:]) == 0: return False
    key = "default"
    for raw in sys.argv[1:]:
        if raw.startswith("-"):
            key = raw
            if key not in data: data[key] = []
        else:
            data[key].append(raw)
    return True

def read(*args):
    if len(args) == 0: return _getVal("default")
    for key in args:
        if key in data: return _getVal(key)
    return None

def readList(*args):
    if len(args) == 0: return data["default"]
    for key in args:
        if key in data: return data[key]
    return None

def _getVal(key): return data[key][0] if len(data[key]) > 0 else ""






