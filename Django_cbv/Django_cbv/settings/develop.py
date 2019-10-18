"""开发环境配置"""
from .base import *  # NOQA
# 其中#NOQA 这个注释的作用是， 告诉PEP 8 规范检测工具，这个地方不需要检测。当然， 我们
# 也可以在一个文件的第一行增加#flakes : NOQA 来告诉规范检测工具，这个文件不用检查。
DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
