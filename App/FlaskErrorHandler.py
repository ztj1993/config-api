# -*- coding: utf-8 -*-
# Intro: 错误处理信息返回模块
# Author: Ztj
# Email: ztj1993@gmail.com

import yaml.scanner

from .Env import *


class FlaskErrorHandler:
    """错误处理对象"""

    @staticmethod
    @FlaskApp.errorhandler(404)
    def error_handler_exception(ex):
        return str('接口不存在'), 404

    @staticmethod
    @FlaskApp.errorhandler(Excepts.CursorNotExist)
    def error_handler_exception(ex):
        return str('游标不存在'), 404

    @staticmethod
    @FlaskApp.errorhandler(Excepts.CursorExisting)
    def error_handler_exception(ex):
        return str('游标已经存在'), 404

    @staticmethod
    @FlaskApp.errorhandler(Excepts.KeyNotExist)
    def error_handler_exception(ex):
        return str('键不存在'), 404

    @staticmethod
    @FlaskApp.errorhandler(json.decoder.JSONDecodeError)
    def error_handler_exception(ex):
        return str('JSON 解析错误'), 500

    @staticmethod
    @FlaskApp.errorhandler(yaml.scanner.ScannerError)
    def error_handler_exception(ex):
        return str('YAML 解析错误'), 500

    @staticmethod
    @FlaskApp.errorhandler(yaml.scanner.ScannerError)
    def error_handler_exception(ex):
        return str('YAML 解析错误'), 500

    @staticmethod
    @FlaskApp.errorhandler(Excepts.RequestShort)
    def error_handler_exception(ex):
        return str('缺失请求参数 %s' % ex), 400
