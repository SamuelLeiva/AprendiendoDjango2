from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), #ruta: /
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'), #buscara a user_posts.html
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), #indicamos que aparezca la primary key entera en la url
    path('post/new/', PostCreateView.as_view(), name='post-create'), #por defecto buscara post_form.html
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), #usa el mismo template que create
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),#buscara por defecto post_confirm_delete.html
    path('about/', views.about, name='blog-about'),
] #urls de nuestra pagina

#por defecto PostListView.as_view() busca <app>/<model>_<viewtype>.html
#app = blog  model = post, viewtype=list ==> blog_postlist.html