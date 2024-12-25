from django.urls import path

urlpatterns =[
    path('createtoy/', views.createtoy, name='createtoy'),
    path('viewtoyslist/', views.viewtoyslist, name='viewtoyslist'),
    path('viewtoy/', views.viewtoy, name='viewtoy'),
    path('generategift', views.generategift, name='generategift'),
]