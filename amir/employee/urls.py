from django.urls import path,include

from . import views
from django.contrib.auth import views as auth_views
from rest_framework.routers import SimpleRouter
from .views import employeeView

router=SimpleRouter()
router.register('employees',employeeView)
urlpatterns=router.urls

# urlpatterns=[
#     path('',views.employeeView.as_view(),name="myemployee"),
#     # path('login',views.post_login,name="login"),
    
    

# ]
