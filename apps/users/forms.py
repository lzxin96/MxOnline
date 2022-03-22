# _*_ coding:utf-8 _*_
from django import forms


class LoginForm(forms.Form):
    # 变量名必须与html文件控件名一致
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
