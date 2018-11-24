from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views as core_views

app_name = 'account'
urlpatterns = [
    # specify URL patterns for login, logout and new user registration ('signup')
    url(r'^login/$', auth_views.LoginView.as_view(template_name="account/login.html"), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="account/logged_out.html"), name="logout"),
    url(r'^signup/$', core_views.signup, name='signup'),
]
