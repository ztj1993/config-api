# 环境变量转 INI 配置接口

## 应用示例
```
$ export FRP_COMMON_SERVER_ADDR=0.0.0.0
$ export FRP_COMMON_BIND_PORT=7000
$ export FRP_SSH_TYPE=tcp
$ export FRP_SSH_LOCAL_IP=127.0.0.1
$ export FRP_SSH_LOCAL_PORT=22
$ export FRP_SSH_REMOTE_PORT=6000

$ data=$(env | grep FRP) && echo "${data}"

    FRP_COMMON_SERVER_ADDR=0.0.0.0
    FRP_COMMON_BIND_PORT=7000
    FRP_SSH_TYPE=tcp
    FRP_SSH_LOCAL_IP=127.0.0.1
    FRP_SSH_LOCAL_PORT=22
    FRP_SSH_REMOTE_PORT=6000

$ query_args="prefix=FRP&delimiter=_&section_lower=1&key_lower=1"
$ curl -H "Content-Type: text/plain" http://127.0.0.1:5000/env_to_ini?${query_args} -d "${data}"

    [common]
    server_addr = 0.0.0.0
    bind_port = 7000

    [ssh]
    local_ip = 127.0.0.1
    remote_port = 6000
    local_port = 22
    type = tcp

```

## 接口文档
- 接口路径：/env_to_ini
- 返回数据：INI 配置文件文本

参数名|类型|必填|说明
---|---|---|---
prefix|query|否|前缀，只处理指定前缀的环境变量
delimiter|query|否|分隔符，默认下划线，用于分割前缀、配置组和配置键
section_lower|query|否|配置组是否转为小写
key_lower|query|否|配置键是否转为小写
-|data|是|环境变量文本数据
