from rest_framework import routers
from post.views import PostViewset

router = routers.DefaultRouter()
router.register(r'posts', PostViewset)