from django.urls import path
from . import views

urlpatterns=[
    path('', views.index,name='list'),
	path('update_task/<str:pk>/', views.updateTask, name="update_task"),
	path('delete/<str:pk>/', views.deleteTask, name="delete"),
	path('main',views.mainpage),
	path('main2',views.mainpage1),
	path('about',views.aboutus),
	path('insert', views.insert),
	path('reg', views.reg),
	path('login', views.login),
	path('log_ch', views.log_check),
]


