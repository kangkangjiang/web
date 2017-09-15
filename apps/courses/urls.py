from django.conf.urls import url,include
from .views import CourseListView,CourseDetailView,CourseLearnView,CourseCommentView,AddCommentView
urlpatterns = [
    # 课程机构首页
    url(r'^list/',CourseListView.as_view(), name="course_list"),
    #课程详情页
    url(r'^detail(?P<course_id>\d+)/',CourseDetailView.as_view(), name="course_detail"),
    #  章节信息
    url(r'^learn(?P<course_id>\d+)/', CourseLearnView.as_view(), name="course_learn"),
    #课程评论
    url(r'^comment(?P<course_id>\d+)/', CourseCommentView.as_view(), name="course_comment"),
    #添加评论
    url(r'^addcomment',AddCommentView.as_view(), name="addcomment"),

]