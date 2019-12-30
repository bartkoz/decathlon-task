from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter

from api.views import MovieViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('comments/', views.CommentAPIView.as_view(), name='comments'),
    path('top/', views.TopAPIView.as_view(), name='top'),
    ]

urlpatterns += router.urls
