from django.conf.urls import url,include
from .views import Orglistview,UserAskView,Org_homeView,Org_CourseListViwe,\
    Org_DescView,Org_TeacherView,UserFavoriteView,TeacherlistView,TeacherDetailView
urlpatterns = [
    # 课程机构首页
    url(r'^listr/',Orglistview.as_view(), name="org_list"),
    # 教师首页
    url(r'^teacher_listr/', TeacherlistView.as_view(), name="org_teacher_list"),
    # 教师详情页
    url(r'^teacher_detail/(?P<teacher_id>\d+)', TeacherDetailView.as_view(), name="org_teacher_detail"),
    url(r'^add/',UserAskView.as_view(), name="add"),
    # 机构详情页
    url(r'^home/(?P<org_id>\d+)/$', Org_homeView.as_view(), name="org_home"),
#     机构课程列表页
    url(r'^courses/(?P<org_id>\d+)/', Org_CourseListViwe.as_view(), name="org_courses"),
#    机构介绍页
    url(r'^desc/(?P<org_id>\d+)/', Org_DescView.as_view(), name="org_desc"),
#   讲师页
    url(r'^teacher/(?P<org_id>\d+)/', Org_TeacherView.as_view(), name="org_teacher"),
# 用户收藏
    url(r'^addfav/',UserFavoriteView.as_view(),name="adfav"),
]