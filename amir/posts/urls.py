from django.urls import path, include

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.post_list, name="posts"),
    # path('login',views.post_login,name="login"),
    path('register', include('users.urls')),
    path('login', auth_views.LoginView.as_view(
        template_name='posts/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(
        template_name='posts/logout.html'), name='logout'),

    path('create', views.post_create, name="create"),
    path('<slug>', views.post_detail, name="detail"),
    path('<slug>/edit', views.post_update, name="update"),
    path('<id>/delete', views.post_delete, name="delete"),


]
