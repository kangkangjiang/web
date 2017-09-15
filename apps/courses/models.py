from django.db import models
from datetime import datetime
from orgnization.models import CourseOrg,Teacher
# Create your models here.
class Courses(models.Model):
    courses_org=models.ForeignKey(CourseOrg,null=True,blank=True)
    teacher=models.ForeignKey(Teacher,null=True,blank=True)
    name=models.CharField(max_length=20,verbose_name="课程名")
    desc=models.CharField(max_length=300,verbose_name="课程描述")
    detail=models.TextField(verbose_name="课程详情")
    degree=models.CharField(max_length=100,choices=(("cj","初级"),("zj","中级"),("gj","高级")))
    lear_time=models.IntegerField(default=0,verbose_name="学习时长")
    students=models.IntegerField(default=0,verbose_name="学习人数")
    fav_nums=models.IntegerField(default=0,verbose_name="收藏人数")
    image=models.ImageField(upload_to="courses/%y/%m",verbose_name="封面")
    clik_nums=models.IntegerField(verbose_name="点击数")
    category=models.CharField(default="后端开发",verbose_name='课程类别',max_length=50)
    tag=models.CharField(default="",verbose_name='课程标签',max_length=10)
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")
    you_know=models.CharField(default='',max_length=100,verbose_name='课程须知')
    teacher_tell=models.CharField(default='',max_length=100,verbose_name='老师告诉你能学到什么')
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name="课程"
        verbose_name_plural=verbose_name
    # 获取全部章节数
    def get_zj_nums(self):
        return self.lesson_set.all().count()
    # 获取全部章节
    def get_zj(self):
        return self.lesson_set.all()
    # 学习人数
    def learn_nums(self):
        return self.usercourse_set.all()[:3]


class Lesson(models.Model):
    courses=models.ForeignKey(Courses,verbose_name="课程")
    name=models.CharField(max_length=100,verbose_name="章节名")
    lesson_nums=models.IntegerField(max_length=10,default=1,verbose_name="课程章节数")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name="章节"
        verbose_name_plural=verbose_name
    def get_video(self):
        return self.video_set.all()
    def __str__(self):
        return str(self.name)

class Video(models.Model):
    lesson=models.ForeignKey(Lesson,verbose_name="章节")
    name=models.CharField(max_length=100,verbose_name="视频名")
    time=models.IntegerField(max_length=50,verbose_name="视频时长",default=50)
    url=models.CharField(max_length=100,default='',verbose_name='视频地址')
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name="视频"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class CoureseResource(models.Model):
    courses=models.ForeignKey(Courses,verbose_name="课程",default=0)
    name=models.CharField(max_length=100,verbose_name="名称")
    download=models.FileField(upload_to="courses/resource/%Y/%m")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name="课程资源"
        verbose_name_plural=verbose_name
    def __str__(self):
        return str(self.name)