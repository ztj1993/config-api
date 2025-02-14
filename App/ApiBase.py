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
    @FlaskApp.route('/', methods=['GET', 'POST'])
    def api_root():
        return 'ok'

    @staticmethod
    @FlaskApp.route('/init', methods=['GET', 'POST'])
    def cursor_init():
        """初始化游标"""
        delimiter = str(flask.request.values.get('delimiter', '.'))
        expire = int(flask.request.values.get('expire', 300))

        cursor_id = MemoryData.init_cursor(delimiter)
        MemoryData.set_cursor_expire(cursor_id, expire)

        return str(cursor_id)

    @staticmethod
    @FlaskApp.route('/env_to_ini', methods=['GET', 'POST'])
    def env_to_ini():
        """初始化游标"""
        prefix = flask.request.values.get('prefix')
        delimiter = str(flask.request.values.get('delimiter', '_'))
        section_lower = bool(flask.request.values.get('section_lower', False))
        key_lower = bool(flask.request.values.get('key_lower', False))
        env_str = str(flask.request.get_data().decode())

        return Libs.env_to_ini(
            env_str,
            prefix=prefix,
            delimiter=delimiter,
            section_lower=section_lower,
            key_lower=key_lower
        )
