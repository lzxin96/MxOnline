# _*_ coding:utf-8 _*_
import xadmin

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    # 页面你显示字段名
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students']
    # 搜索
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    # 过滤器
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students']


xadmin.site.register(Course, CourseAdmin)