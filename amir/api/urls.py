from rest_framework.routers import SimpleRouter
from .views import PostView

router=SimpleRouter()
router.register('posts',PostView)
urlpatterns=router.urls