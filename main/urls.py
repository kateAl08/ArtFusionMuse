from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('myacc/', views.my_account, name='myacc'),
    path('arts/<int:post_id>/', views.newarts, name='arts'),
    path('logout/', LoginUser.as_view(), name='logout'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('add/', AddPage.as_view(), name='add_page'),

]