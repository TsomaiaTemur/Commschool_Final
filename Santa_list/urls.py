from django.urls import path

urlpatterns = [
    path('createlist/', views.createlist, name='createlist'),
    path('viewlist/', views.viewlist, name='viewlist'),
    path('deletekid/', views.deletekid, name='deletekid'),
    path('createkid/', views.createkid, name='createkid'),
    path('viewkidlist/', views.viewkidlist, name='viewkidlist'),
    path('viewkid', views.viewkid, name='viewkid'),
]