from django.shortcuts import HttpResponse

# Create your views here.
from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import isAuthor


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

    permission_classes = [IsAuthenticated, isAuthor]
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

