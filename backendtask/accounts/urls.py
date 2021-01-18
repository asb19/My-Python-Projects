from django.urls import path
from .views import RegisterView, LoginView, FavouriteAddApi,UserProfileDetailsApi


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('addfavourite', FavouriteAddApi.as_view()),
    path('userprofile', UserProfileDetailsApi.as_view()),
]