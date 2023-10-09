from django.urls import path
from authentication.views import register_user,login_user,logout_user,update_user
app_name='authentication'
urlpatterns = [
    path('login/',login_user, name='login'),
    path('register/',register_user,name='register'),
    path('logout/',logout_user,name='logout'),
    path('update/',update_user,name='update_user')
]