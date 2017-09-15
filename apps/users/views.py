import json
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from users.utils.email_send import send_register_email
from .models import EmailVerifyRecord
from users.forms import Updataimage,UserInfoForms
from users.utils.mixin_utils import LoginRequiredMixin
from operation.models import UserCourse,UserFavorite,UserMessage
from users.forms import RegisterForms,UserLoginForms,ModifPwdForms
from .models import UserProfile,EmailVerifyRecord
from orgnization.models import CourseOrg,Teacher
from courses.models import Courses


class UserMessageView(View):
    '''
    用户消息
    '''
    def get(self,request):
        all_message=UserMessage.objects.filter(user=request.user.id)
        # 清除用户未读消息
        all_un_read=UserMessage.objects.filter(user=request.user.id,has_read=False)
        for un_read in all_un_read:
            un_read.has_read=True
            un_read.save()
        # 分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        objects = ['john', 'edward', 'josh', 'frank']
        # 需要传入默认值  5
        p = Paginator(all_message, 3, request=request)
        message = p.page(page)

        return render(request,'usercenter-message.html',{
            'all_message':message,

        })


class UserFavCourseView(LoginRequiredMixin,View):
    '''
    用户收藏课程
    '''
    def get(self,request):
        course_list=[]
        # 拿到了用户收藏的课程为一个列表
        user_fav_course = UserFavorite.objects.filter(user=request.user,fa_type=1)
        for fav_teacher in user_fav_course:
            course_id=fav_teacher.favid
            course=Courses.objects.get(id=course_id)
            course_list.append(course)
        return render(request,'usercenter-fav-course.html',{
            "course_list":course_list,
        })

class UserFavTeacherView(LoginRequiredMixin,View):
    '''
    用户收藏教师
    '''
    def get(self,request):
        Teacher_list=[]
        # 拿到了用户收藏的机构为一个列表
        user_fav_teacher = UserFavorite.objects.filter(user=request.user,fa_type=2)
        for fav_teacher in user_fav_teacher:
            teacher_id=fav_teacher.favid
            teacher=Teacher.objects.get(id=teacher_id)
            Teacher_list.append(teacher)
        return render(request,'usercenter-fav-teacher.html',{
            "Teacher_list":Teacher_list,
        })

class UserFavOrgView(LoginRequiredMixin,View):
    '''
    用户收藏机构
    '''
    def get(self,request):
        org_list=[]
        # 拿到了用户收藏的机构为一个列表
        user_fav_org = UserFavorite.objects.filter(user=request.user,fa_type=3)
        for fav_org in user_fav_org:
            org_id=fav_org.favid
            org=CourseOrg.objects.get(id=int(org_id))
            org_list.append(org)
        return render(request,'usercenter-fav-org.html',{
            "org_list":org_list,
        })

class UserCourseView(LoginRequiredMixin,View):
    '''
    用户课程
    '''
    def get(self,request):
        user_course=UserCourse.objects.filter(user=request.user)
        return render(request,'usercenter-mycourse.html',{
            "user_courses":user_course,

        })

class UpdataInfoView(LoginRequiredMixin,View):
    '''
    修改用户信息
    '''
    def get(self,request):
        return render(request,'usercenter-info.html')
    def post(self,request):
        # 必须要标明实例的对象，不然会新创建一个实例
        user_info_forms=UserInfoForms(request.POST,instance=request.user)
        if user_info_forms.is_valid():
            user_info_forms.save()
            return HttpResponse('{"status":"success"}', content_type="application/json")
        else:
            return HttpResponse('{"status":"fail"}', content_type="application/json")


class UpDataEmailView(LoginRequiredMixin,View):
    '''
    修改邮箱
    '''
    def post(self,request):
        eamil=request.POST.get('email','')
        code=request.POST.get('code','')

        existed_code=EmailVerifyRecord.objects.filter(code=code)
        if existed_code:
            user=request.user
            user.email=eamil
            user.save()
            return HttpResponse('{"status":"success"}', content_type="application/json")
        else:
            return HttpResponse('{"email":"验证码错误"}', content_type="application/json")






class SendEmailView(LoginRequiredMixin,View):
    '''
    发送邮箱验证码
    '''
    def get(self,request):
        email=request.GET.get('email','')
        if UserProfile.objects.filter(email=email):
            return HttpResponse({'email':"邮箱已注册"},content_type="application/json")
        send_register_email(email, "updata")
        return HttpResponse('{"status":"success"}', content_type="application/json")






class UpLoadPwdView(LoginRequiredMixin,View):
    '''
    用户修改密码
    '''
    def post(self,request):
        modify_form=ModifPwdForms(request.POST)
        if modify_form.is_valid():
            pw1=request.POST.get('password1','')
            pw2 = request.POST.get('password2', '')
            if pw1!=pw2:
                return HttpResponse('{"status":"fail","msg":"密码不一致"}', content_type="application/json")
            user=request.user
            user.password=make_password(pw2)
            user.save()

            return HttpResponse('{"status":"success"}', content_type="application/json")
        else:
            return HttpResponse(json.dumps(modify_form.errors) , content_type="application/json")

class UserLoadImageView(LoginRequiredMixin,View):
    #用户更新头像
    def post(self,request):
       #  通过instance实例化,可以直接保存传来的文件
        image_form=Updataimage(request.POST,request.FILES,instance=request.user)
        if image_form.is_valid():
            # image=image_form.changed_data['image']
            image_form.save()
            return HttpResponse('{"status":"success"}', content_type="application/json")
        else:
            return HttpResponse('{"status":"fail"}', content_type="application/json")


class UserListView(LoginRequiredMixin,View):
    #用户中心首页
    def get(self,request):
        user=request.user
        return render(request,'usercenter-info.html',{
            "user":user,

        })
class CustomBackend(ModelBackend):
    # 判断是否登录
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user=UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

class UserLogoutView(View):
    '''
    用户登出
    '''
    def get(self,request):
        logout(request)
        from django.core.urlresolvers import reverse
        return HttpResponseRedirect(reverse('index'))

class UserLogin(View):
    '''
    用户登录
    '''
    def post(self,request):
        user_name=request.POST.get("username",None)
        pass_word = request.POST.get("password", None)
        # 判断user是否为真，为真即存在该用户
        user_loginform=UserLoginForms(request.POST)
        if user_loginform.is_valid():
            uesr = authenticate(username=user_name,password=pass_word)
            if uesr is not None :
                if uesr.is_active:
                    login(request,uesr)
                    return HttpResponseRedirect("/index")
                else:
                    return render(request, "login.html", {"msg": "没有激活"})
            else:
                return render(request,"login.html",{"msg":"输入错误"})
        else:
            return render(request,"login.html",{"msg":user_loginform})
    def get(self,request):
        return render(request, "login.html")

class Activeuserview(View):
    '''
    # 激活验证
    '''
    def get(self,request,active_code):
        all_records=EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email=record.email
                user=UserProfile.objects.get(email=email)
                user.is_active=True
                user.save()
                return render(request,"login.html")
        else:
            return HttpResponse("验证码错误啊")
class RegisterView(View):
    '''
    邮箱注册验证
    '''
    def get(self, request):
        register_form = RegisterForms()
        return render(request,"register.html",{"register_form":register_form})
    def post(self,request):
        register_form=RegisterForms(request.POST)
        if register_form.is_valid():
            register_form = RegisterForms(request.POST)
            user_name=request.POST.get("email",None)
            if UserProfile.objects.filter(email=user_name) is None:
                password=request.POST.get("password",None)
                print(user_name,password)
                user_profile=UserProfile()
                user_profile.is_active=False
                user_profile.email=user_name
                user_profile.username=user_name
    #            对传进来的铭文密码进行加密
                user_profile.password=make_password(password)
                send_register_email(user_name,"register")
                user_profile.save()
                # 发送消息，用户注册成功
                user_message=UserMessage()
                user_message.user=user_profile.id
                user_message.message='欢迎注册康康在线网'
                user_message.save()
                return render(request,"login.html")
            else:
                return render(request,"register.html",{"msg":"用户已经存在","register_form":register_form})
        else:
            return render(request,"register.html",{"register_form":register_form})

