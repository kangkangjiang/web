from django.shortcuts import render,HttpResponse
from django.views.generic.base import View
from .models import Courses,CourseOrg,CoureseResource
from operation.models import AddComment,UserCourse,UserFavorite
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from users.utils.mixin_utils import LoginRequiredMixin
from django.db.models import Q
# Create your views here.
class AddCommentView(View):
    '''
    增加评论
    '''
    def post(self,request):
        if not request.user.is_authenticated():
            return HttpResponse('{"status":"fail","msg":"用户未登录"}', content_type="application/json")
        course_id = request.POST.get('course_id',0)
        comment=request.POST.get('comments','')
        if int(course_id)>0 and comment:
            course_comment=AddComment()
            course=Courses.objects.get(id=int(course_id))
            course_comment.course=course
            course_comment.comment=comment
            course_comment.user=request.user
            course_comment.save()
            return HttpResponse('{"status":"success","msg":"评论成功"}', content_type="application/json")
        else:
            return HttpResponse('{"status":"fail","msg":"评论成功"}', content_type="application/json")
class CourseCommentView(LoginRequiredMixin,View):
        """
        课程评论
        """
        def get(self,request,course_id):
            course = Courses.objects.get(id=int(course_id))
            all_courserourse = CoureseResource.objects.filter(courses=course)
            all_comment=AddComment.objects.all()
            return render(request,'course-comment.html',{
                "course": course,
                "resource": all_courserourse,
                "all_comment":all_comment,

            })
class CourseLearnView(LoginRequiredMixin,View):
    """
    公开课详细
    """
    def get(self,request,course_id):
        course=Courses.objects.get(id=int(course_id))
        # 首先查询一下，是否已经记录
        user_courses=UserCourse.objects.filter(courses=course,user=request.user)
        if not user_courses:
            user_courses=UserCourse(courses=course,user=request.user)
            user_courses.save()

        user_courses=UserCourse.objects.filter(courses=course)
        # 通过user_course拿到user。ID，，拿到所有用户ID
        user_ids=[user_course.user.id for user_course in user_courses]
        # 有外键关联，通过user加下划线_,id  再加双下划线__匹配user_ids列表里面的ID
        all_user_course=UserCourse.objects.filter(user_id__in=user_ids)
        course_ids = [user_course.courses.id for user_course in all_user_course]
        relation_course=Courses.objects.filter(id__in=course_ids).order_by('-clik_nums')[:2]
        all_courserourse=CoureseResource.objects.filter(courses=course)
        return render(request,'course-video.html',{
            "course":course,
            "resource":all_courserourse,
            'relation_course':relation_course,

        })
class CourseDetailView(View):
    """
    课程详情
    """
    def get(self,request,course_id):
        course=Courses.objects.get(id=int(course_id))
        # 判断收藏状态与否
        has_fav = False
        has_org_fav=False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, favid=int(course.id), fa_type=1):
                has_fav = True
            if UserFavorite.objects.filter(user=request.user, favid=int(course.courses_org.id), fa_type=3):
                has_org_fav=True
        # 增加课程点击数
        course.clik_nums +=1
        course.save()
        # 相关课程推荐
        tag=course.tag
        if tag:
            relate_course=Courses.objects.filter(tag=tag)[:1]
        else:
            relate_course=[]
        return render(request,'course-detail.html',{
            "detail":course,
            "relate_course":relate_course,
            'has_fav':has_fav,
            'has_org_fav':has_org_fav,
        })
class CourseListView(View):
    """
    课程列表页
    """
    def get(self,request):
        all_courses=Courses.objects.all().order_by("-add_time")
        hot_courses = Courses.objects.all().order_by("-clik_nums")
        # 搜索
        search_keywords=request.GET.get('keywords','')
        if search_keywords:
            all_courses=Courses.objects.filter(Q(name__icontains=search_keywords)|
                                               Q(desc__icontains=search_keywords)|
                                               Q(detail__icontains=search_keywords)|
                                               Q(tag__icontains=search_keywords))
        # 筛选
        sort=request.GET.get("sort","")
        if sort:
            if sort:
                if sort == "hot":
                    all_courses = all_courses.order_by("-fav_nums")
                elif sort == "students":
                    all_courses = all_courses.order_by("-students")
        # 分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        objects = ['john', 'edward', 'josh', 'frank']
        # 需要传入默认值  5
        p = Paginator(all_courses, 6, request=request)
        courses = p.page(page)
        #     注意通过分页后的courses不是QUERSITE类型
        return render(request,'course-list.html',{
            "all_courses":courses,
            "sort":sort,
            "hot_course":hot_courses,

        })
