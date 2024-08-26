from django.urls import path
from myapp import views


urlpatterns = [
    path('users',views.getUsers),
    path('create/',views.addUser),
    path('read/<str:pk>',views.getUser),
    path('update/<str:pk>',views.updateUser),
    path('delete/<str:pk>',views.deleteUser),
    
]