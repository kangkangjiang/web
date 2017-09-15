from django.shortcuts import render
from django.views.generic.base import View
from .models import CityDict,CourseOrg,Teacher,Orgcate
from django.shortcuts import render,HttpResponse
from django.db import models
from django.shortcuts import render_to_response
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from operation.models import UserFavorite,UserAsk
from django.db.models import Q
from  courses.models import Courses

# Create your views here.
class TeacherDetailView(View):
    '''
    教师详情页
    '''
    def get(self,request,teacher_id):
        teacher=Teacher.objects.get(id=int(teacher_id))
        # 增加点击数
        teacher.clik_nums+=1
        teacher.save()
        all_teacher=Teacher.objects.all()
        hot_teacher=all_teacher.order_by('-clik_nums')[:2]
        all_courses=teacher.courses_set.all()
        return render(request,'teacher-detail.html',{
                "teacher":teacher,
                'all_courses':all_courses,
                'hot_teacher':hot_teacher,
        })
class TeacherlistView(View):
    '''
    教师列表页
    '''
    def get(self,request):
        # 所有教师
        all_teacher=Teacher.objects.all()
        # 搜索
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_teacher = Teacher.objects.filter(Q(name__icontains=search_keywords) |
                                               Q(work_position__icontains=search_keywords) |
                                               Q(work_years__icontains=search_keywords)
                                               )
        # 人气进行筛选
        sort=request.GET.get('sort','')
        if sort:
            if sort=='hot':
                all_teacher=all_teacher.order_by('-work_years')
        # 人气讲师，通过clik_nums
        hot_teacher=all_teacher.order_by('-clik_nums')[:3]
        # 统计人数
        all_count=all_teacher.count()
        # 分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        objects = ['john', 'edward', 'josh', 'frank']
        # 需要传入默认值  5
        p = Paginator(all_teacher, 3, request=request)
        teacher = p.page(page)

        return render(request,'teachers-list.html',{
            # 经过分页后，“all_teacher”不在是querset类型，，
            # 变成Page类型，不能迭代 所以前端页面需要在all_teacher后面再加.object_list
            "all_teacher":teacher,
            "hot_teacher":hot_teacher,
            'sort':sort,
            "all_count":all_count,

        })

class Orglistview(View):
    """
    课程机构首页
    """
    def get(self,request):
        # 城市
        all_city=CityDict.objects.all()
        # 课程机构
        all_org=CourseOrg.objects.all()
        hot_org=all_org.order_by("clik_nums")[:4]
        # 搜索
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_org = CourseOrg.objects.filter( Q(name__icontains=search_keywords) |
                                                Q(desc__icontains=search_keywords) |
                                                Q(city__icontains=search_keywords)
                                                )
        # 课程机构类别
        all_cat=Orgcate.objects.all( )
        # 取出筛选的城市
        city_id = request.GET.get('city', "")
        if city_id:
            # 注意得到的是字符串，要转换成int型
            all_org = CourseOrg.objects.filter(city_id=int(city_id))
        # 取出筛选的机构类别
        catgroy_id=request.GET.get("catgroy_id","")
        if catgroy_id:
            all_org = CourseOrg.objects.filter(catgroy_id=int(catgroy_id))
        # 双重帅选
        if catgroy_id and city_id:
            all_org = CourseOrg.objects.filter(city_id=int(city_id),catgroy_id=int(catgroy_id))
        all_count = all_org.count()
        # 通过SORT判断是对学习人数筛选还是课程筛选
        sort=request.GET.get("sort","")
        if sort:
            if sort=="students":
                all_org=all_org.order_by("-syudent")
            elif sort=="courses":
                all_org=all_org.order_by("-courses_nums")

        # 分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
           page = 1
        objects = ['john', 'edward', 'josh', 'frank']
        # 需要传入默认值  5
        p = Paginator(all_org,3,request=request)
        orgs = p.page(page)

        return render(request,"org-list.html",{
            "all_city":all_city,
            "all_course":orgs,
            "all_count":all_count,
            "city_id": city_id,
            "catgroy_id":catgroy_id,
            "all_cat":all_cat,
            "hot_org":hot_org,
            "sort":sort,
        })

from orgnization.forms import UserAskForm
from django.views.generic.base import View
from django.http import HttpResponse
from users.utils.mixin_utils import LoginRequiredMixin
# # Create your views here.
class UserFavoriteView(View):
   """
   用户收藏
    """
   def post(self,request):
        favid=request.POST.get("fav_id",0)
        fa_type = request.POST.get("fav_type", 0)
        # 判断用户是否存在
        if  not request.user.is_authenticated():
            return HttpResponse('{"status":"fail","msg":"用户未登录"}',content_type="application/json")
        # favid 和fa_type  必须同时判断
        exist_records=UserFavorite.objects.filter(user=request.user,favid=int(favid),fa_type=int(fa_type))
        if exist_records:
            # 如果exist_records 存在表示用户取消收藏
            # 收藏数减一
            if int(fa_type) == 1:
                course = Courses.objects.get(id=favid)
                course.fav_nums -= 1
                if course.fav_nums==0:
                    course.fav_nums=0
                    course.save()
            elif int(fa_type) == 2:
                teacher = Teacher.objects.get(id=favid)
                teacher.fav_nums -= 1
                if teacher.fav_nums==0:
                    teacher.fav_nums=0
                    teacher.save()
            elif int(fa_type) == 3:
                org = CourseOrg.objects.get(id=favid)
                org.fav_nums -= 1
                if org.fav_nums==0:
                    org.fav_nums=0
                    org.save()
            exist_records.delete()
            return HttpResponse('{"status":"fail","msg":"收藏"}', content_type="application/json")
        user_fav=UserFavorite()
        if int(favid)>0 and int(fa_type)>0:
            # 收藏数加一
            if int(fa_type)==1 :
                course=Courses.objects.get(id=favid)
                course.fav_nums+=1
                course.save()
            elif int(fa_type)==2 :
                teacher=Teacher.objects.get(id=favid)
                teacher.fav_nums+=1
                teacher.save()
            elif int(fa_type)==3:
                org=CourseOrg.objects.get(id=favid)
                org.fav_nums+=1
                org.save()
            user_fav.user=request.user
            user_fav.favid=int(favid)
            user_fav.fa_type=int(fa_type)
            user_fav.save()
            return HttpResponse('{"status":"success","msg":"收藏成功"}', content_type="application/json")


class Org_TeacherView(View):
    """
    机构教师页
    """
    def get(self,request,org_id):
        current_page = "teacher"
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 判断收藏状态与否
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, favid=int(course_org.id), fa_type=3):
                has_fav = True
        all_teacher=course_org.teacher_set.all()
        return render(request, "org-detail-teachers.html", {
            "course_org": course_org,
            "current_page": current_page,
            "all_teacher":all_teacher,
            'has_fav': has_fav,
        })
class Org_DescView(View):
    """
      机构介绍页
      """
    def get(self,request,org_id):
        current_page = "desc"
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 判断收藏状态与否
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, favid=int(course_org.id), fa_type=3):
                has_fav = True
        return render(request, "org-detail-desc.html", {
            "course_org": course_org,
            "current_page": current_page,
            'has_fav': has_fav,
        })
class Org_CourseListViwe(View):
    """
      机构课程页
      """
    def get(self, request,org_id):
        current_page = "course"
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 判断收藏状态与否
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, favid=int(course_org.id), fa_type=3):
                has_fav = True
        all_courses = course_org.courses_set.all()
        return render(request, "org-detail-course.html", {
            "course_org": course_org,
            "all_courses": all_courses,
            "current_page": current_page,
            'has_fav': has_fav,

        })
class Org_homeView(View):
    """
      机构主页
      """
    def get(self,request,org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 机构点击次数加一
        course_org.clik_nums+=1
        course_org.save()
        # 判断收藏状态与否
        has_fav=False
        if  request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user,favid=int(course_org.id),fa_type=3):
                has_fav = True
        current_page="home"
        all_courses=course_org.courses_set.all()
        all_teacher=course_org.teacher_set.all()
        return render(request,"org-detail-homepage.html",{
            "current_page":current_page,
            "course_org":course_org,
            "all_courses":all_courses,
            "all_teacher":all_teacher,
            'has_fav':has_fav,
        })

class UserAskView(View):
    """
        用户咨询
    """
    def post(self, request):
            userask_form = UserAskForm(request.POST)
            username=request.POST.get('name','')
            usermobile=request.POST.get('mobile',"")
            courses=request.POST.get('course_name','')
            print(usermobile,username)
            if userask_form.is_valid():
                # 通过commit=true 才能将数据保存导数据库里
                # userask_ask = userask_form.save(commit=True)
                #             返回数据返回的是jason，异步的操作,,,指定返回的格式content_type="application/json
                userask=UserAsk()
                userask.name=username
                userask.mobile=usermobile
                userask.courses_name=courses
                userask.save()
                return HttpResponse({"status": "success"}, content_type="application/json")
            else:
                return HttpResponse({'status':'fail','msg':'添加出错'}, content_type="application/json")
