"""生产环境配置"""
from .base import *  # NOQA
# 其中#NOQA 这个注释的作用是， 告诉PEP 8 规范检测工具，这个地方不需要检测。当然， 我们
# 也可以在一个文件的第一行增加#flakes : NOQA 来告诉规范检测工具，这个文件不用检查。
DEBUG = False

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# 数据库相关配置 MySQL数据库的配置方法
DATABASES = {
    'default': {
        # 链接数据库类型
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': '123456',
    }
}
