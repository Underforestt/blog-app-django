from django.urls import path
from . import views


urlpatterns = [
    path('', views.showblog, name='showblog'),
    path('<int:post_id>/', views.post_full, name='post_full'),
]