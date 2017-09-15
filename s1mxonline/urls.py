"""s1mxonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from users.views import UserLogin,RegisterView,Activeuserview,UserLogoutView
import xadmin
from django.views.generic import TemplateView
from orgnization.views import Orglistview,TeacherlistView
from django.views.static import serve
from s1mxonline.settings import MEDIA_ROOT
urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^index/', TemplateView.as_view(template_name="index.html"),name="index"),
    url(r'^login/',UserLogin.as_view(),name="login"),
    # 退出登录
    url(r'^logout/', UserLogoutView.as_view(), name="logout"),
    url(r'^register/',RegisterView.as_view(),name="register"),
    # 拿到随机字符串
    url(r'^captcha/', include("captcha.urls")),
    url(r'^active/(?P<active_code>.*)/',Activeuserview.as_view(),name="active"),
#     配置个人中心页面
    url(r'^user/', include("users.urls", namespace="user")),
# 机构相关URL配置
    url(r'^orglistr/',include("orgnization.urls",namespace="org")),
# 课程相关URL的配置
    url(r'^courses/', include("courses.urls", namespace="courses")),

#  导入静态文件的处理方法
    url(r'^media/(?P<path>.*)',serve,{"document_root":MEDIA_ROOT}),
]
