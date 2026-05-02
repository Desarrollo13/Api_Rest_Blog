from rest_framework.routers import DefaultRouter
from comments.api.views import CommentApiViewSet

router_comment=DefaultRouter()
router_comment.register(prefix='comments',basename='comments',viewset=CommentApiViewSet)