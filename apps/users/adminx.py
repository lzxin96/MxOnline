# _*_ coding:utf-8 _*_
import xadmin

from .models import EmailVerifyRecord, Banner


class EmailVerifyRecordAdmin(object):
    # 变量名不可变
    # 页面你显示字段名
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索
    search_fields = ['code', 'email', 'send_type']
    # 过滤器
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    # 页面你显示字段名
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    # 搜索
    search_fields = ['title', 'image', 'url', 'index']
    # 过滤器
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
