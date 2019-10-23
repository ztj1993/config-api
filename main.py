# -*- coding: utf-8 -*-
# Intro: 入口模块
# Author: Ztj
# Email: ztj1993@gmail.com

import os

from App.ApiBase import ApiBase
from App.ApiCursor import CursorBlueprint
from App.ApiMonitor import MonitorBlueprint
from App.Env import *
from App.FlaskErrorHandler import FlaskErrorHandler

ApiBase = ApiBase
FlaskErrorHandler = FlaskErrorHandler

FLASK_HOST = os.getenv("FLASK_HOST", "127.0.0.1")
FLASK_PORT = os.getenv("FLASK_PORT", 5000)

if __name__ == '__main__':
    FlaskApp.register_blueprint(CursorBlueprint)
    FlaskApp.register_blueprint(MonitorBlueprint)
    FlaskApp.run(host=FLASK_HOST, port=FLASK_PORT, threaded=True)
