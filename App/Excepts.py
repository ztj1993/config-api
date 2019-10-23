# -*- coding: utf-8 -*-
# Intro: 异常模块
# Author: Ztj
# Email: ztj1993@gmail.com

class ExceptionBase(Exception):
    """基础异常"""
    pass


class CursorNotExist(ExceptionBase):
    """游标不存在"""
    pass


class CursorExisting(ExceptionBase):
    """游标已经存在"""
    pass


class KeyNotExist(ExceptionBase):
    """键不存在"""
    pass


class RequestShort(ExceptionBase):
    """缺少请求参数 Key"""
    pass
