from django.urls import path
from .views import index, login_view, logout_view, change_pas, createuser, editProfile
urlpatterns = [
    path('', index , name = 'index'),
    path('login/', login_view , name = 'login'),
    path('logout/', logout_view , name = 'logout'),
    path('change_password/', change_pas , name = 'change_pas'),
    path('create_user/', createuser , name = 'createuser'),
    path('edit_profile/', editProfile , name = 'editProfile')
]
