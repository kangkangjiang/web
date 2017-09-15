from django.db import models
from datetime import datetime
from users.models import UserProfile
from courses.models import Courses

class UserMessage(models.Model):
    '''
    用户消息表
    '''
    user=models.IntegerField(default=0,verbose_name='接受用户')
    message=models.CharField(default='',max_length=500,verbose_name='消息内容')
    has_read=models.BooleanField(default=False,verbose_name='是否已阅读')
    add_time=models.DateTimeField(default=datetime.now,verbose_name='当前时间')

    class Meta:
        verbose_name='用户消息'
        verbose_name_plural=verbose_name
    def __str__(self):
        user_message=UserProfile.objects.get(id=self.user)
        return user_message.username



class AddComment(models.Model):
    course=models.ForeignKey(Courses ,max_length=50, verbose_name="课程名")
    user=models.ForeignKey(UserProfile ,max_length=50, verbose_name="用户名字")
    comment=models.CharField(max_length=200,verbose_name='评论内容')
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")
    class Meta:
        verbose_name = "用户评论"
        verbose_name_plural = verbose_name

class UserAsk(models.Model):
    name = models.CharField(max_length=50, verbose_name="用户名字")
    mobile=models.CharField(max_length=11, verbose_name="电话")
    courses_name=models.CharField(max_length=50, verbose_name="课程名字")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")
    class Meta:
        verbose_name="用户咨询"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name
class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile ,max_length=50, verbose_name="用户名字")
    favid=models.IntegerField(default=1,max_length=50,verbose_name="数据ID")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")
    fa_type=models.IntegerField(choices=((1,"课程"),(2,"讲师"),(3,"机构")),max_length=50,default=1)

    class Meta:
        verbose_name = "收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username

class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile,max_length=50, verbose_name="用户名字")
    courses=models.ForeignKey(Courses,max_length=50,verbose_name="课程")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Mate:
        verbose_name = "用户课程"
        verbose_name_plural = verbose_name
