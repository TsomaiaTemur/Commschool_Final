from django.urls import path

urlpatterns = [
    path('countkids', views.countkids, name='countkids'),
    path('viewdemand', views.viewdemand, name='viewdemand'),
    path('viewproduction', views.viewproduction, name='viewproduction'),
    path('viewcourier', views.viewcourier, name='viewcourier'),
]