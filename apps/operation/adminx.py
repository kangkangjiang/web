import xadmin
from .models import UserFavorite,UserMessage
class UserFavoriteAdmin(object):
    pass
class UserMeassageAdmin(object):
    pass
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(UserMessage,UserMeassageAdmin)