from django.urls import path
from .views import board_main, board_list, board_write, board_detail, test, apart, predict

app_name = "boards"

urlpatterns = [
    path('', board_main, name='board_main'),
    path('list/', board_list, name='board_list'),
    path('write/', board_write, name='board_write'),
    path('detail/<int:pk>/', board_detail, name='board_detail'),
    path('test', test, name="test"),
    path('apart', apart, name="apart"),
    path('predict', predict, name="predict"),
]