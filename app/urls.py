from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('register_test/', views.register_view, name='register_test'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('home/time_entry_create/', views.time_entry_create, name='time_entry_create'),
    path('home/time_entry/', login_required(views.TimeEntryModelList.as_view(), login_url='login'), name='time_entry'),
]
