# -*- coding: utf-8 -*-
# Intro: 库模块
# Author: Ztj
# Email: ztj1993@gmail.com

import configparser
from io import StringIO

from dotenv import dotenv_values


def env_to_ini(env_str, prefix=None, delimiter='_', section_lower=False, key_lower=False):
    """环境变量文本转 INI 文本"""
    ini_parser = configparser.ConfigParser()
    # 解析环境变量
    file_stream = StringIO(env_str)
    file_stream.seek(0)
    items = dotenv_values(stream=file_stream)
    for item in items:
        # 提取关键元素
        words = item.split(delimiter)
        if len(words) < 3:
            continue
        if prefix is not None:
            # 校验前缀
            item_prefix = words.pop(0)
            if not item_prefix == prefix:
                continue
        section = words.pop(0)
        key = delimiter.join(words)
        value = items.get(item)
        # 设置关键元素
        section = section.lower() if section_lower else section
        key = key.lower() if key_lower else key
        if not ini_parser.has_section(section):
            ini_parser.add_section(section)
        ini_parser.set(section, key, value)
    # 输出 INI 文本
    output_stream = StringIO()
    ini_parser.write(output_stream)
    return output_stream.getvalue()
