from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, PostViewSet, CommentViewSet


router = DefaultRouter()
router.register(r'api/v1/posts', PostViewSet, basename='posts')
router.register(r'api/v1/groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path(
        'api/v1/posts/<int:post_id>/comments/',
        CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='comments-list'
    ),
    path(
        'api/v1/posts/<int:post_id>/comments/<int:comment_id>/',
        CommentViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='comments-detail'
    ),
]
