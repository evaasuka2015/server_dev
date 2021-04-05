from django.conf.urls import url
from . import views

# ~/login/regist_user
urlpatterns = [
    url('regist_user', views.RegistUser.as_view(), name='regist_user'),
    url('app_login', views.AppLogin.as_view(), name='app_login'),
]
