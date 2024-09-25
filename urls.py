"""
URL configuration for instagram project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from insta import views
from instagram import settings

urlpatterns = [
    path('ulogin/',views.ulogin),
    path('ulogin_post/',views.ulogin_post),
    path('register/',views.register),
    path('register_post/',views.register_post),
    path('changepasw/',views.changepasw),
    path('changepasw_post/',views.changepasw_post),
    path('view_registration/',views.view_registration),
    path('edit/',views.edit),
    path('edit_post/',views.edit_post),
    path('home/',views.home),
    path('send_complaint/',views.send_complaint),
    path('send_complaintpost/',views.send_complaintpost),
    path('view_reply/',views.view_reply),
    path('post/', views.post),
    path('post_post/', views.post_post),
    path('usersearch/', views.usersearch),
    path('user_search_results/',views.user_search_results),
    path('frequest/',views.frequest),
    path('usersend_feedback/',views.usersend_feedback),
    path('usersend_feedback_post/',views.usersend_feedback_post),
    path('reportuser/<id>',views.reportuser),
    path('reportuser_post/',views.reportuser_post),
    path('ahome/',views.adminhome),
    path('adminusers/',views.adminusers),
    path('adminusersearch/',views.adminusersearch),
    path('adminview_complaint/',views.adminview_complaint),
    path('adminview_feedback/',views.adminview_feedback),
    path('admindatesearch_post/',views.admindatesearch_post),
#     path('adminviewcom/',views.adminviewcom),
#     path('send_reply_post/',views.send_reply_post),
#     path('compsearch_post/',views.compsearch_post),
#     path('adminchangepasw/',views.adminchangepasw),
#     path('adminchangepasw_post/',views.adminchangepasw_post)
]