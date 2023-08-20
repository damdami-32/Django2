from django.urls import path, include
from .views import register, login, logout
from boards.views import test, apart as boards_views
from boards import urls

app_name = "accounts"

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('boards/', include('boards.urls')),
]