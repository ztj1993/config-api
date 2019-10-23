# Config Api

这是一个配置 restful api 接口，是一个 json yaml restful 接口。

项目主要解决在命令行下操作 json, yaml 配置文件问题。

## 项目功能
- 通过 API 接口操作配置项
- 上传 JSON, YAML 配置文件
- 操作 JSON, YAML 配置项(增删改查)
- 输出 JSON, YAML 配置文件

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
```
$ data=$(cat /etc/docker/daemon.json) && echo ${data}

    {
        "registry-mirrors": ["http://ef017c13.m.daocloud.io"]
    }

$ cursor_id=$(curl -sf http://127.0.0.1:5000/init) && echo ${cursor_id}

    158853936809905161020585456234816085535

$ curl http://127.0.0.1:5000/${cursor_id}/load/json -d "${data}"

    ok

$ curl http://127.0.0.1:5000/${cursor_id}/set/bool?key=tlsverify -d "true"
$ curl http://127.0.0.1:5000/${cursor_id}/set/str?key=tlscacert -d "/etc/certs/ca.pem"
$ curl http://127.0.0.1:5000/${cursor_id}/set/str?key=tlscert -d "/etc/certs/server-cert.pem"
$ curl http://127.0.0.1:5000/${cursor_id}/set/str?key=tlskey -d "/etc/certs/server-key.pem"
$ curl http://127.0.0.1:5000/${cursor_id}/append/str?key=hosts -d "tcp://0.0.0.0:2376"
$ curl http://127.0.0.1:5000/${cursor_id}/append/str?key=hosts -d "unix:///var/run/docker.sock"

    ok

$ curl http://127.0.0.1:5000/${cursor_id}/output/json

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
