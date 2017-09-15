import xadmin
from xadmin import views
from .models import UserProfile, EmailVerifyRecord, Banner
class BaseSetting(object):
    """
    基础设置，主题
    """
    enable_themes = True
    use_bootswatch = True
class GlobalSetting(object):
    """
    标题，按钮收缩
    """
    site_title="康康后台管理系统"
    site_footer="康康在线网"
    menu_style="accordion"


class EmailVerifyRecordAdmin(object):
    #设置列表显示，，收索文件，，
    list_display=["code","email","send_type"]
    search_fields=["code","email","send_type","send_time"]
    list_filter=["code","email","send_type"]
class BannerAdmin(object):
    pass
# class UserProfileAdmin(object):
#     pass
# xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
# 设置后台管理的主题
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)
