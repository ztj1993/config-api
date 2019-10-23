# -*- coding: utf-8 -*-
# Intro: 基本接口模块
# Author: Ztj
# Email: ztj1993@gmail.com

import threading

from .Env import *


class ApiBase:
    """基本接口"""

    @staticmethod
    @FlaskApp.before_first_request
    def memory_clear_listen():
        """内存清理监听"""
        threading.Thread(target=MemoryData.clear_listen, args=()).start()

    @staticmethod
    @FlaskApp.route('/init', methods=['GET', 'POST'])
    def cursor_init():
        """初始化游标"""
        delimiter = str(flask.request.values.get('delimiter', '.'))
        expire = int(flask.request.values.get('expire', 300))

        cursor_id = MemoryData.init_cursor(delimiter)
        MemoryData.set_cursor_expire(cursor_id, expire)

        return str(cursor_id)
