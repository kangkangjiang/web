from .models import Courses,CoureseResource,Lesson,Video
import xadmin
class VideoAdmin(object):
    pass
class CoursesAdmin(object):
    list_display = ["name", "desc", "detail","degree","lear_time","students"]
    # search_fields = ["code", "email", "send_type", "send_time"]
    # list_filter = ["code", "email", "send_type"]
class CoureseResourceAdmin(object):
    list_display = ["courses", "name", "download",]
    search_fields = ["courses", "name", "download",]
class LessonAdmin(object):
    list_display = ["courses", "name", "lesson_nums", 'add_time']
    search_fields = ["courses", "name", "lesson_nums", 'add_time']
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(CoureseResource,CoureseResourceAdmin)
xadmin.site.register(Courses,CoursesAdmin)
xadmin.site.register(Video,VideoAdmin)