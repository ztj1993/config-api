# -*- coding: utf-8 -*-
# Intro: 监控接口模块
# Author: Ztj
# Email: ztj1993@gmail.com

from .Env import *

MonitorBlueprint = flask.Blueprint('ApiMonitor', __name__, url_prefix='/monitor')


class ApiMonitor:
    """监控接口"""

    @staticmethod
    @MonitorBlueprint.route('/cursors', methods=['GET', 'POST'])
    def cursors():
        """获取内存游标键"""
        return json.dumps(list(MemoryData.CursorData.keys()), indent=4)

    @staticmethod
    @MonitorBlueprint.route('/expires', methods=['GET', 'POST'])
    def expires():
        """获取失效数据"""
        return json.dumps(MemoryData.ExpireData, indent=4)
