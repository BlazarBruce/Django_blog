from django.db import models

# 此处要创建用户认证表
class userInfo(models.Model):
    user_id = models.IntegerField(verbose_name="id")
    user_name = models.CharField(max_length=100, verbose_name="name")
    user_token = models.CharField(max_length=100, verbose_name="token")

    class Meta:
        # 重新定义表名.
        db_table = 'user_info'
