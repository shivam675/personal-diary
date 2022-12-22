from django.urls import path
from log import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # path('', views.home, name='hello_world'),
    # path('add', views.enter_log, name='enter_log'),
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'), 
    # path('current/', views.currenttodos, name='currenttodos'),
    path('create/', views.create_log, name='create_log'),
    path('log/<int:log_pk>', views.view_logs, name='view_logs'),
    # path('todo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('log/<int:log_pk>/delete', views.delete_logs, name='deletetodo'),
    path('all_logs/', views.view_all_logs, name='view_all_logs'),
]