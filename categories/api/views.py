from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly

class CategoryApiViewSet(ModelViewSet):
    permission_classes=[IsAdminOrReadOnly]
    serializer_class= CategorySerializer
    # queryset=Category.objects.all()
    # voy filtrar por los que este publicado con True
    queryset=Category.objects.filter(published=True)
    # que busque por la palabra slub
    lookup_field='slug'
    filter_backends=[DjangoFilterBackend]
    # con este moodulo que intale ahora puedo filtrar con este array
    filterset_fields=['published','title']
