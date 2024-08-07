from django.urls import path
from . import views

app_name = 'myblog'

urlpatterns = [
    path('', views.index, name="blog-index"),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]
