# -*- coding: utf-8 -*-
# Intro: 入口模块
# Author: Ztj
# Email: ztj1993@gmail.com

from App.ApiBase import ApiBase
from App.ApiCursor import CursorBlueprint
from App.ApiMonitor import MonitorBlueprint
from App.Env import *
from App.FlaskErrorHandler import FlaskErrorHandler

ApiBase = ApiBase
FlaskErrorHandler = FlaskErrorHandler

if __name__ == '__main__':
    FlaskApp.register_blueprint(CursorBlueprint)
    FlaskApp.register_blueprint(MonitorBlueprint)
    FlaskApp.run(threaded=True)
