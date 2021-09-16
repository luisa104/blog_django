from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import PostDetailView, PostListView, PostCreateView, PostDeleteView, PostUpdateView

urlpatterns = [
    path('post/', PostListView.as_view(), name='post'),
    path('post/agregar/', PostCreateView.as_view(), name="post_create"),
    path('post/<slug:slug>/', PostDetailView.as_view(), name="post_detail"),
    path('post/editar/<slug:slug>/', PostUpdateView.as_view(), name="post_update"),
    path('post/eliminar/<slug:slug>/', PostDeleteView.as_view(), name="post_delete"),
]