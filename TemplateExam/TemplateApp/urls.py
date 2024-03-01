from django.urls import path
from . views import home, member, members

app_name = 'app'
urlpatterns = [
    path('home/',home, name='home'),
    path('members/',members, name= 'members'),
    path('member/<int:id>', member, name= 'member'),
    ]