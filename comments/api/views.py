from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


from comments.models import Comment
from comments.api.serializers import CommentSerializer
from comments.api.permissions import IsOwnerOrReadAndCreateOnly


class CommentApiViewSet(ModelViewSet):
    # agrego los permisos
    permission_classes=[IsOwnerOrReadAndCreateOnly]
    serializer_class=CommentSerializer
    queryset=Comment.objects.all()
    # quiero ordenar los comments los mas nuevos arriba y los mas antiguo a bajo
    filter_backends=[OrderingFilter,DjangoFilterBackend]
    # le digo por los campos que quiero ordenar
    ordering=['-create_at']
    # aca voy filtrar poe un posts especifico
    filterset_fields=['posts']
   