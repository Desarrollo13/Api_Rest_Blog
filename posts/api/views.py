from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Post
from posts.api.serializers import PostSerializer
from posts.api.permissions import IsAdminOrReadOnly


class PostApiViewSet(ModelViewSet):
    permission_classes=[IsAdminOrReadOnly]
    serializer_class=PostSerializer
    queryset=Post.objects.filter(published=True)
    lookup_field='slug'
    # para poder filtrar a cada post por categoria
    filter_backends=[DjangoFilterBackend]
    # aca puedo filtrar por el id y a la vez tambien por slug
    filterset_fields=['category','category__slug']
    # padre filtra por el id de la categoria
    # filterset_fields=['category']