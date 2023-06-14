from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('login/',views.LoginView.as_view(),name='userlogin'),
    path('',views.DashBoardView.as_view(),name='dashboard'),
    path('userlist/',views.UserListView.as_view(),name='userlist'),
    path('userlogout/',views.UserLogoutView.as_view(),name='userlogout'),
    path('userregistrationform/',views.UserRegistrationView.as_view(),name = 'userregistration'),
    path('userstatus/<int:id>/',views.UserStatusView.as_view(),name = 'userstatus'),
    path('usersettings/',views.UserSettingsView.as_view(),name='usersettings'),
]
