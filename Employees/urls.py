from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index,name='index'),
    path('',views.index,name='index'),
    path('view_all',views.view_all,name='view_all'),
    path('add_emp',views.add_emp,name='add_emp'),
    path('filter_emp',views.filter_emp,name='filter_emp'),
    path('remove_emp',views.remove_emp,name='remove_emp'),
    path('remove_emp/<int:emp_id>',views.remove_emp,name='remove_emp'),

]