# -*- coding: utf-8 -*-
# Intro: 内存数据模块
# Author: Ztj
# Email: ztj1993@gmail.com

import math

from .Env import *


class MemoryData:
    """内存数据对象"""
    CursorData = dict()
    ExpireData = dict()
    expire_key_divisor = 60

    @staticmethod
    def get_cursor_id():
        """获取游标编号"""
        return uuid.uuid4().int

    def init_cursor(self, delimiter='.') -> int:
        """初始化游标"""
        cursor_id = self.get_cursor_id()
        cursor_target = registry.Registry()
        cursor_target.separator = delimiter
        rs_target = self.CursorData.setdefault(cursor_id, cursor_target)
        if not cursor_target == rs_target:
            raise Excepts.CursorExisting()
        return cursor_id

    def get_cursor_target(self, cursor_id) -> registry.Registry:
        """获取游标对象"""
        cursor_target = self.CursorData.get(cursor_id)
        if not isinstance(cursor_target, registry.Registry):
            raise Excepts.CursorNotExist()
        return cursor_target

    def delete_cursor(self, cursor_id):
        """删除游标"""
        return self.CursorData.pop(cursor_id, False)

    def store_expire_key(self, expire_time):
        """存储有效期键"""
        return math.ceil(expire_time / self.expire_key_divisor)

    def delete_expire_key(self, expire_time):
        """删除有效期键"""
        return int(expire_time / self.expire_key_divisor)

    def init_expire(self, expire_time):
        """初始化有效期"""
        key = self.store_expire_key(expire_time)
        self.ExpireData.setdefault(key, list())

    def set_cursor_expire(self, cursor_id, expire=300):
        """设置游标有效期"""
        cur_time = int(time.time())
        expire_time = cur_time + expire
        self.init_expire(expire_time)
        self.get_expire(expire_time).append(cursor_id)

    def get_expire(self, expire_time) -> list:
        """获取有效期列表"""
        key = self.store_expire_key(expire_time)
        return self.ExpireData.get(key)

    def pop_expire(self, expire_time) -> list:
        """弹出有效期"""
        key = self.delete_expire_key(expire_time)
        return self.ExpireData.pop(key, False)

    def clear(self, clear_time):
        """清理内存"""
        cursor_ids = self.pop_expire(int(clear_time))
        if cursor_ids is False:
            return False
        for cursor_id in cursor_ids:
            self.delete_cursor(cursor_id)
        return True

    def clear_listen(self):
        """清理内存监听"""
        while True:
            self.clear(int(time.time()))
            time.sleep(self.expire_key_divisor / 2)
