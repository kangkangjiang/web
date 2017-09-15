from users.models import EmailVerifyRecord
from random import Random
from django.core.mail import send_mail
from s1mxonline.settings import EMAIL_FROM
def random_str(randomlength=8):
    str=""
    chars="abcefghijklmnopqrstruvwxyz0123456789"
    length=len(chars)-1
    random=Random()
    for i in range(randomlength):
        str+=chars[random.randint(0,length)]
    return str

def send_register_email(email,send_type="register"):
    email_recode=EmailVerifyRecord()
    if send_type=='updata':
        code=random_str(4)
    else:
        code = random_str(16)
    # 保存邮箱的code
    email_recode.code=code
    email_recode.email=email
    email_recode.send_type=send_type
    email_recode.save()
    email_title=" "
    email_body=" "
    if send_type=="register":
        email_title="康康在线网注册激活链接 "
        email_body=" 请点击下面的链接激活注册：http://127.0.0.1:8000/active/{0}".format(code)

# 调用send_mail
        send_status=send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_status:
            pass
    # elif send_type == "register":
    #     email_title = "康康在线网注册激活链接 "
    #     email_body = " 请点击下面的链接激活注册：http://127.0.0.1:8000/active/{0}".format(code)
    #
    #         # 调用send_mail
    #     send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
    #     if send_status:
    #         pass
    elif send_type == "updata":
        email_title = "康康在线网更新邮箱激活链接 "
        email_body = " 请输入一下四位验证码进行验证》》》》》{0}".format(code)

            # 调用send_mail
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass