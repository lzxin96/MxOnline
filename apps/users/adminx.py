# _*_ coding:utf-8 _*_
import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


class BaseSetting(object):
    # 开启主题设置，使用views注册
    enable_themes = True
    use_bootswatch = True


# 全局设置
class GlobalSettings(object):
    site_title = '暮学后台管理系统'
    site_footer = '暮学在线网'
    # 导航栏显示样式
    menu_style = 'accordion'


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
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
