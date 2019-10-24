# Config Api

这是一个 config restful api 接口。

主要解决在命令行下操作 json, yaml, ini 等配置文件问题。

## 项目功能
- 通过 API 接口操作配置文件
- 支持 JSON, YAML 配置文件的增删改查
- 输出 JSON, YAML 配置文件
- 支持将环境变量转为 INI 配置文件

## 项目地址
- Github(国外)：https://github.com/ztj1993/config-api.git
- Gitee(国内)：https://gitee.com/zhangtianjie/config-api.git

## 项目运行
```
pip install -r requirements.txt
python main.py
```

```
docker pull ztj1993/config-api
docker run  -d --name config-api -p 5000:5000 ztj1993/config-api
```

## 使用示例

> JSON 配置文件操作示例

```
$ uri=http://127.0.0.1:5000

$ #获取配置原始数据
$ data=$(cat /etc/docker/daemon.json) && echo ${data}

    {
        "registry-mirrors": ["http://ef017c13.m.daocloud.io"]
    }

$ #初始化配置游标
$ cursor_id=$(curl -fsS ${uri}/init) && echo ${cursor_id}

    158853936809905161020585456234816085535

$ cursor_uri=${uri}/${cursor_id}

$ #将配置上传到游标
$ curl ${cursor_uri}/load/json -d "${data}"

    ok

$ #操作配置
$ curl -H "Content-Type: text/plain" ${cursor_uri}/set/bool?key=tlsverify -d "true"
$ curl -H "Content-Type: text/plain" ${cursor_uri}/set/str?key=tlscacert -d "/etc/certs/ca.pem"
$ curl -H "Content-Type: text/plain" ${cursor_uri}/set/str?key=tlscert -d "/etc/certs/server-cert.pem"
$ curl -H "Content-Type: text/plain" ${cursor_uri}/set/str?key=tlskey -d "/etc/certs/server-key.pem"
$ curl -H "Content-Type: text/plain" ${cursor_uri}/append/str?key=hosts -d "tcp://0.0.0.0:2376"
$ curl -H "Content-Type: text/plain" ${cursor_uri}/append/str?key=hosts -d "unix:///var/run/docker.sock"

    ok

$ #输出配置
$ curl ${cursor_uri}/output/json

    {
        "registry-mirrors": [
            "http://ef017c13.m.daocloud.io"
        ],
        "tlsverify": true,
        "tlscacert": "/etc/certs/ca.pem",
        "tlscert": "/etc/certs/server-cert.pem",
        "tlskey": "/etc/certs/server-key.pem",
        "hosts": [
            "tcp://0.0.0.0:2376",
            "unix:///var/run/docker.sock"
        ]
    }

```

> 环境变量生成 INI 配置文件示例

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

## 文档说明
- [接口文档](Docs/Api.md)

## TODO
- 数据请求长度限制
- 游标数据大小限制
- 引入环境变量支持
- 改善部署方式

## 项目贡献
本项目是一个开源项目，欢迎任何人为其开发和进步贡献力量。
- 在使用过程中出现任何问题，请通过 [Issue](https://github.com/ztj1993/config-api/issues) 反馈
- Bug 修复可以直接提交 Pull Request 到 develop 分支
- 如果您有任何其他方面的问题，欢迎邮件至 ztj1993@gmail.com 交流
