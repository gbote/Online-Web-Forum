from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('post/<int:post_id>',views.post_detail, name='post_detail'),
    path('new_post', views.new_post, name="new_post"),
]