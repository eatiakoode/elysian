# myapp/urls.py
from django.urls import path
from .views import RegisterView, LoginView,UserListView 

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('users/', UserListView.as_view(), name='users'),

]

