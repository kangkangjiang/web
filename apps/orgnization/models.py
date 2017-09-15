#_*_ coding: utf-8 _*_
from django.db import models
from datetime import datetime
# from courses.models import Courses
# Create your models here.
class Orgcate(models.Model):
    name=models.CharField(max_length=50,verbose_name="机构类别")
    add_time=models.DateTimeField(default=datetime.now,)
    class Meta:
        verbose_name="机构类别"
        verbose_name_plural=verbose_name
    def __str__(self):
          return  self.name

class CityDict(models.Model):
    name=models.CharField(max_length=50,verbose_name="城市名称")
    desc=models.TextField(verbose_name="城市描述")
    add_time=models.DateTimeField(default=datetime.now,)
    class Meta:
        verbose_name="城市名称"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name
class CourseOrg(models.Model):
    name=models.CharField(max_length=50,verbose_name="机构名称")
    catgroy=models.ForeignKey(Orgcate,max_length=100,default="1",verbose_name="机构类别")
    desc=models.TextField(verbose_name="机构描述")
    syudent=models.IntegerField(default=0,verbose_name="学习人数")
    clik_nums=models.IntegerField(default=0,verbose_name="点击数")
    fav_nums=models.IntegerField(default=0,verbose_name="收藏数")
    image=models.ImageField(upload_to="org/%Y/%M",max_length=100,verbose_name="封面图")
    city=models.ForeignKey(CityDict,verbose_name="所在城市")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")
    # courses=models.CharField(max_length=100,verbose_name="经典课程",default="")
    # courses = models.ForeignKey(Courses,max_length=100,default="1")
    courses_nums=models.IntegerField(default=1,verbose_name="课程数",max_length=20)
    class Meta:
        verbose_name="机构名称"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

    # 老师人数
    def get_teacher_nums(self):
      return  self.teacher_set.all().count()

class Teacher(models.Model):
    org=models.ForeignKey(CourseOrg,verbose_name="所属机构")
    name = models.CharField(max_length=50, verbose_name="教师姓名")
    work_years=models.IntegerField(default=0,verbose_name="工作年限")
    work_company= models.CharField(max_length=50, verbose_name="工作地址")
    work_position=models.CharField(max_length=50, verbose_name="职位")
    points=models.CharField(max_length=50, verbose_name="教学特点")
    clik_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    age=models.IntegerField(default=20, verbose_name="年龄")
    image = models.ImageField(upload_to="teacher/%Y/%M", max_length=100, verbose_name="教师照片",default="")
    add_time=models.DateTimeField(default=datetime.now,)

    class Meta:
        verbose_name="教师"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

    def get_nums_teacher(self):
        #统计老师课程总数
        return self.courses_set.all().count()

class UserAsk(models.Model):
    name = models.CharField(max_length=50, verbose_name="用户名字")
    mobile=models.CharField(max_length=11, verbose_name="电话")
    course_name=models.CharField(max_length=50, verbose_name="课程名字")
    add_time=models.DateTimeField(default=datetime.now,verbose_name="添加时间")
    class Meta:
        verbose_name="用户咨询"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name