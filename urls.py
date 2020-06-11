
from django.contrib import admin
from django.urls import path,re_path
from . import  views
from .models import  Entry
from .views import indexView,ArticleDetail,post,Profile
from django.contrib.auth import  views  as auth_views
from .apps import FormsaConfig

#app_name='formsa'
app_name = FormsaConfig.name

urlpatterns = [
    path('',indexView.as_view(), name='index'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('post/', views.post, name='post'),
    path('article/<int:pk>',ArticleDetail.as_view(template_name='formsa/detail.html'), name='article-detail'),
    path("profile/", views.profile, name="profile"),

    # #reset password stuff
    # # path('^', include('django.contrib.auth.urls'))
    #  #path('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),
    # # path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_sent'),
    #  #path('password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # # path('reset_password_done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_done'),
    # path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    # path('reset_password_done/', auth_views.PasswordResetDoneView, name='password_reset_done'),
    # path('password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # path('reset_done/', auth_views.PasswordResetCompleteView, name='password_reset_complete'),
]