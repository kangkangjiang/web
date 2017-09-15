from .models import CourseOrg,CityDict,Teacher,Orgcate
import xadmin
from .models import UserAsk
class UserAskAdmin(object):
    pass
xadmin.site.register(UserAsk,UserAskAdmin)
class CityDictAdmin(object):
        list_display = ["name", "desc", "add_time", ]
        search_fields = ["name", "desc", "add_time", ]
        list_filter = ["name", "desc", "add_time", ]
class CourseOrgAdmin(object):
    list_display = ["name", "desc","fav_nums","image" ,"city","add_time"]
    search_fields = ["name", "desc","fav_nums","image" ,"city"]
    list_filter = ["name", "desc","fav_nums","image" ,"city","add_time"]

class TeacherAdmin(object):
    list_display = ["org","name", "work_years", "work_company","points","work_position","fav_nums","add_time"]
    search_fields =  ["org","name", "work_years", "work_company","points","work_position","fav_nums",]
    list_filter =  ["org","name", "work_years", "work_company","points","work_position","fav_nums","add_time"]
class OrgcateAdmin(object):
    list_display = ["name"]
xadmin.site.register(Orgcate,OrgcateAdmin)
xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)

