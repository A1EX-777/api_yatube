from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import GroupViewSet, PostViewSet, CommentViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/comments/',
         CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='comments-list'),
    path('posts/<int:post_id>/comments/<int:pk>/',
         CommentViewSet.as_view({
             'get': 'retrieve',
             'put': 'update',
             'patch': 'partial_update',
             'delete': 'destroy'
         }),
         name='comments-detail'),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
]