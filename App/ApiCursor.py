# -*- coding: utf-8 -*-
# Intro: 游标接口模块
# Author: Ztj
# Email: ztj1993@gmail.com

from .Env import *

CursorBlueprint = flask.Blueprint('ApiCursor', __name__, url_prefix='/<int:cursor_id>')


class ApiCursor:
    """游标接口"""

    @staticmethod
    def req_key():
        """请求键"""
        key = flask.request.values.get('key')
        if key is None:
            raise Excepts.RequestShort('key')
        return key

    @staticmethod
    def req_data(data_type):
        """请求数据"""
        if data_type == 'str':
            val = str(flask.request.get_data().decode())
        elif data_type == 'int':
            val = int(flask.request.get_data().decode())
        elif data_type == 'bool':
            val = flask.request.get_data().decode()
            val = True if val == 'true' else False
        elif data_type == 'json':
            val = json.loads(flask.request.get_data())
        elif data_type == 'yaml':
            val = yaml.load(flask.request.get_data())
        else:
            val = flask.request.get_data().decode()
        return val

    @staticmethod
    @CursorBlueprint.url_value_preprocessor
    def init_cursor_target(endpoint, values):
        """初始化游标数据"""
        cursor_id = values.pop('cursor_id')
        flask.g.cursor_target = MemoryData.get_cursor_target(cursor_id)

    @staticmethod
    @CursorBlueprint.route('/set/<data_type>', methods=['GET', 'POST'])
    def set(data_type):
        """设置数据"""
        key = ApiCursor.req_key()
        data = ApiCursor.req_data(data_type)

        flask.g.cursor_target.set(key, data)
        return 'ok'

    @staticmethod
    @CursorBlueprint.route('/append/<data_type>', methods=['GET', 'POST'])
    def append(data_type):
        """追加数据"""
        key = ApiCursor.req_key()
        data = ApiCursor.req_data(data_type)

        flask.g.cursor_target.append(key, data)
        return 'ok'

    @staticmethod
    @CursorBlueprint.route('/unset', methods=['GET', 'POST'])
    def unset():
        """删除数据"""
        key = ApiCursor.req_key()
        flask.g.cursor_target.unset(key, clear=True)
        return 'ok'

    @staticmethod
    @CursorBlueprint.route('/get/<data_type>', methods=['GET', 'POST'])
    def get(data_type):
        """获取数据"""
        key = ApiCursor.req_key()
        val = flask.g.cursor_target.get(key)

        if data_type == 'json':
            return json.dumps(val, indent=4)
        elif data_type == 'yaml':
            return yaml.dump(val)
        elif data_type == 'str':
            return str(val)
        else:
            raise flask.abort(404)

    @staticmethod
    @CursorBlueprint.route('/output/<data_type>', methods=['GET', 'POST'])
    def output(data_type):
        """输出数据"""
        val = flask.g.cursor_target.get()

        if data_type == 'json':
            return json.dumps(val, indent=4)
        elif data_type == 'yaml':
            return yaml.dump(val)
        else:
            raise flask.abort(404)

    @staticmethod
    @CursorBlueprint.route('/load/<data_type>', methods=['GET', 'POST'])
    def load(data_type):
        """加载数据"""
        if data_type == 'json':
            data = json.loads(flask.request.get_data())
        elif data_type == 'yaml':
            data = yaml.load(flask.request.get_data())
        else:
            raise flask.abort(404)

        flask.g.cursor_target.load(data)
        return 'ok'

    @staticmethod
    @CursorBlueprint.route('/key/<operator>', methods=['GET', 'POST'])
    def key(operator):
        """键操作"""
        key = ApiCursor.req_key()
        val = flask.g.cursor_target.get(key)

        if val is None:
            raise Excepts.KeyNotExist()
        elif operator == 'exist':
            return 'ok'
        elif operator == 'type':
            return type(val)
