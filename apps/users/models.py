from django.db import models
from datetime import datetime
# Create your models here.
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    nick_name=models.CharField(max_length=50,default="",verbose_name="英文名字")
    birday=models.CharField(max_length=64,verbose_name="生日")
    address=models.CharField(max_length=100,verbose_name="地址")
    gender=models.CharField(choices=(("male","男"),("female","女")),max_length=30,)
    mobile=models.IntegerField(default=0,max_length=12,verbose_name='用户电话')
    image=models.ImageField(upload_to="image/%y/%m",default="image/default.png",max_length=100)
    email = models.CharField(max_length=100,default='',verbose_name='邮箱')
    class Meta:
        verbose_name="用户信息哦"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.username
    # 判断消息是否已已读
    def get_has_read(self):
        from operation.models import UserMessage
        return UserMessage.objects.filter(user=self.id,has_read=False).count()
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name="验证码")
    email=models.EmailField(max_length=50,verbose_name="邮箱")
    send_type=models.CharField(choices=(("register","注册"),("forget","找回密码"),("updata","修改邮箱")),max_length=10)
    send_time=models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name="邮箱验证码"
        verbose_name_plural=verbose_name
class Banner(models.Model):
    title=models.CharField(max_length=100,verbose_name="标题")
    image=models.ImageField(upload_to="banner/%Y/%M",max_length=100,verbose_name="轮播图")
    url=models.URLField(max_length=50,verbose_name="访问地址")
    index=models.IntegerField(default=100,verbose_name="顺序")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")
    class Meta:
        verbose_name="轮播图"
        verbose_name_plural=verbose_name