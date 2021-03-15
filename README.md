```bash
.
├── .flake8  # flake8 linter plugin config
├── .gitlab-ci.yml  # gitlab CI/CD ，可以添加各种自动化规则
├── .pre-commit-config.yaml  # 在执行git commit命令时，触发执行一系列指定的检查
├── apps  # 各种reusable app，约定：如果是对外服务的app，需要在__init__.py存在bp这个变量
│   ├── auth  # 用户登录，登出
│   │   ├── __init__.py
│   │   ├── models.py  # User/Account models
│   │   ├── parser.py  # input parser
│   │   ├── restful.py  # restful api
│   │   └── urls.py
│   └── __init__.py
├── config  # 各种配置文件，文件名应该清晰的表明配置文件的作用
│   ├── ansible
│   │   ├── deploy-test.yml
│   │   └── hosts
│   ├── nginx.conf
│   ├── supervior.conf
│   └── uwsgi.ini
├── core  # 项目的核心模块
│   ├── app.py  # 创建实例，初始化实例脚本
│   ├── conf  # 处理各种settings，主要是default
│   │   ├── default.py
│   │   ├── __init__.py
│   │   ├── local.py  # 处理线上和测试（开发）环境的不同，不入库，特定环境下才存在
│   │   └── settings.py  # 项目统一引用的配置文件，从default导入默认的配置，尝试从local导入覆盖的配置
│   ├── const.py  # 常量参数
│   ├── ext.py  # 各类flask扩展，统一管理
│   ├── __init__.py
│   ├── logger.py  # 日志logger以及装饰器
│   └── utils.py  # 脚手架
├── logs
│   └── app.log
├── README.md
├── requirements.txt  # 生产环境依赖库版本信息
├── requirements-dev.txt  # 开发环境依赖库版本信息
├── static  # 前端静态文件
├── templates  # 渲染模板
├── tests  # 单元测试
│   └── __init__.py
└── wsgi.py  # 启动脚本
```
