# -*- coding: utf-8 -*-
# Intro: 环境模块
# Author: Ztj
# Email: ztj1993@gmail.com

import json
import time
import uuid

import flask
import registry
import yaml

from . import Excepts
from . import Libs
from .MemoryData import MemoryData

json = json
uuid = uuid
time = time

yaml = yaml
registry = registry

MemoryData = MemoryData()
Excepts = Excepts
Libs = Libs

FlaskApp = flask.Flask('APP')
