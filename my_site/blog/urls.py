from django.urls import path
from . import views

urlpatterns = [
    path("",views.dashboard, name="dashboard"),
    path("posts",views.posts, name="posts"),
    path("post-detail",views.post_detail, name="post_detail")
]
