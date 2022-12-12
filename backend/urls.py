from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
# from .views import ArticleList, ArticleDetails

urlpatterns = [
    # path('articles/', ArticleList.as_view()),
    # path('articles/<slug>', ArticleDetails.as_view())
    path('', include(router.urls))
]
