from django.conf.urls import url,include
from .views import UserListView,UserLoadImageView,UpLoadPwdView,\
                    SendEmailView,UpDataEmailView,UpdataInfoView,\
                    UserCourseView,UserFavOrgView,UserFavTeacherView,\
                    UserFavCourseView,UserMessageView

urlpatterns = [
    # 课程机构首页
    url(r'^list/',UserListView.as_view(), name="user_list"),
    #用户头像
    url(r'^upload/image/', UserLoadImageView.as_view(), name="user_uploadimage"),
    #用户修改密码
    url(r'^upload/pwd/', UpLoadPwdView.as_view(), name="user_uploadpwd"),
    #发送邮箱验证码
    url(r'^send/email/', SendEmailView.as_view(), name="sendemail"),
    #修改邮箱
    url(r'^updata/email/', UpDataEmailView.as_view(), name="updatamail"),
    #修改用户信息
    url(r'^updata/info/', UpdataInfoView.as_view(), name="updatainfo"),
    #用户课程
    url(r'^usercourses/', UserCourseView.as_view(), name="usercourses"),
    #用户收藏机构
    url(r'^userfavorg/', UserFavOrgView.as_view(), name="userfavorg"),
    #用户收藏教师
    url(r'^userfavteacher/', UserFavTeacherView.as_view(), name="userfavteacher"),
    #用户收藏课程
    url(r'^userfavcourse/', UserFavCourseView.as_view(), name="userfavcourse"),
    #用户消息队列
    url(r'^usermessage/', UserMessageView.as_view(), name="usermessage"),



]