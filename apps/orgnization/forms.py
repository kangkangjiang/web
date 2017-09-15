from django import forms
from django.forms import fields
from orgnization.models import UserAsk

class UserAskForm(forms.Form):
    name = fields.CharField(
        error_messages={"required": "用户名不能为空"}
    )
    mobile = fields.CharField(
        error_messages={"required": "密码不能为空",})
    course_name=fields.CharField(
        error_messages={"required": "密码不能为空",})