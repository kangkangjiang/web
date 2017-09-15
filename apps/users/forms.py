from django import forms
from captcha.fields import CaptchaField
from .models import UserProfile
class UserInfoForms(forms.ModelForm):
    '''
    更改用户信息
    '''
    class Meta:
        model=UserProfile
        fields=['username','birday','gender','mobile','address']
class ModifPwdForms(forms.Form):
    '''
    修改密码
    '''
    password1=forms.CharField(required=True,min_length=6)
    password2= forms.CharField(required=True, min_length=6)

class RegisterForms(forms.Form):
    '''
    登录验证
    '''
    email=forms.EmailField(
       error_messages={"required":"邮箱不能为空"}
    )
    password=forms.CharField(
        error_messages={"required": "邮箱不能为空"}
    )
    captcha=CaptchaField(
        error_messages={"required": "邮箱不能为空"}
    )

class Updataimage(forms.ModelForm):
    '''
    修改头像表单验证
    '''
    class Meta:
        model=UserProfile
        fields=['image']

class UserLoginForms(forms.Form):
    '''
    用户登录表单验证
    '''
    username=forms.CharField(
        error_messages={"required": "用户名不能为空"}
    )
    password=forms.CharField(
        error_messages={"required": "密码不能为空",
                        "max_length":"密码最长为12",
                        "min_length":"密码最短为6",}
    )